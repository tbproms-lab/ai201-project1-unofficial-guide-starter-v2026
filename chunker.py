"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document

# A sentence boundary: end punctuation, then whitespace, then something that
# looks like the start of a new sentence. Good enough for the plain prose in
# these corpora without pulling in a real sentence tokenizer.
_SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])")


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in week 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def _split_into_sentences(text: str) -> list[str]:
    """Break a document into sentences, paragraph by paragraph."""
    sentences: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        for sentence in _SENTENCE_BOUNDARY.split(paragraph):
            sentence = sentence.strip()
            if sentence:
                sentences.append(sentence)
    return sentences


def _pack_sentences(sentences: list[str], chunk_size: int, overlap: int) -> list[str]:
    """
    Greedily pack whole sentences into chunks up to `chunk_size` characters.

    A sentence never gets cut in half — a chunk ends as soon as the next
    sentence would push it over the limit, and the next chunk starts by
    carrying back up to `overlap` characters' worth of trailing sentences,
    so neighbouring chunks still share context. The one exception is a
    single sentence longer than `chunk_size` on its own (a run-on list, say);
    that one gets a hard character split, same as the fallback.
    """
    pieces: list[str] = []
    current: list[str] = []
    current_len = 0

    def flush() -> None:
        if current:
            pieces.append(" ".join(current))

    for sentence in sentences:
        if len(sentence) > chunk_size:
            flush()
            current.clear()
            current_len = 0
            start = 0
            while start < len(sentence):
                piece = sentence[start : start + chunk_size].strip()
                if piece:
                    pieces.append(piece)
                start += chunk_size - overlap
            continue

        added = len(sentence) + (1 if current else 0)
        if current and current_len + added > chunk_size:
            flush()
            # Carry back trailing sentences worth up to `overlap` characters
            # so the new chunk opens with context from the one before it.
            carried: list[str] = []
            carried_len = 0
            for prior in reversed(current):
                extra = len(prior) + (1 if carried else 0)
                if carried and carried_len + extra > overlap:
                    break
                carried.insert(0, prior)
                carried_len += extra
            current = carried
            current_len = carried_len

        current.append(sentence)
        current_len += len(sentence) + (1 if current_len else 0)

    flush()
    return pieces


def split_documents(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    Split documents into chunks along sentence boundaries.

    campus_life posts are short — a paragraph or two, with the useful fact
    usually sitting in a single sentence — so most documents here end up as
    one chunk, same as the fallback gets by coincidence (no post reaches the
    800-character fixed window). The difference shows up on the few longer,
    multi-sentence posts: this splits between sentences instead of wherever
    the character count happens to land, so a chunk never ends mid-thought.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        sentences = _split_into_sentences(doc.text)
        for index, piece in enumerate(_pack_sentences(sentences, chunk_size, overlap)):
            chunks.append(
                Chunk(
                    text=piece,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
