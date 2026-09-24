# The Unofficial Guide

Tolu Bakare - Corpus - advice_threads

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

```
I picked the corpus on advice threads because I liked how the documents for each thread were focused on specific questions. The questions my system answers are related to singular threads and the questions that led to the creation of the thread. The threads were asking by, I assume, new/incoming students wanted to know about campus life, and most questions that were posted were answered by current/past students to help the student with the question understand more about campus life from a personal point of view. It can answer questions like professor email vs office hours, joining clubs, best study spots, commuting by bike, pass or fail, winter clothing, clubs, etc.
```

## Chunking Strategy

**Chunk size: 600 characters **
**Overlap: 100 characters **

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

```
I picked 600 characters because for the corpus I picked, a lot of the threads provided fully good answers for the questions that were asked in the thread. I also chose an overlap of 100 because it doesn't do much, as a lot of the documents questions don't overlap with one another. I had started out with the original 800 chunk size and 120 overlap but felt like it was a bit too long for the advice_threads corpus.
```

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: thread_bike_commute.txt#0 `` — produced by: chunker.py::split_documents ``

```
THREAD: Is a bike worth it for a 20 minute walk commute? --- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three. --- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season. --- reply 3 (22 votes) ---
Both true. I keep a cheap bike for September to November and walk the rest of the year. Total cost was about $120 for the bike and I don't care what happens to it.
```

**Chunk 2** — source: thread_first_gen.txt#0 `` — produced by: chunker.py::split_documents``

```
THREAD: Anything specific for first-generation students? --- reply 1 (33 votes) ---
The advising office has a specific programme and it is genuinely good, but it is opt-in and badly publicised. Ask for it by name. --- reply 2 (41 votes) ---
The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happyto explain them and nobody volunteers them. --- reply 3 (16 votes) ---
Emergency fund for textbooks and travel exists and is not means-tested beyond a short form.
```

**Chunk 3** — source: thread_laptop_specs.txt#0 `` — produced by: chunker.py::split_documents``

```
THREAD: How much laptop do I actually need for CS courses? --- reply 1 (31 votes) ---
Less than the recommended spec page says. 16GB of RAM is the one number worth paying for; everything else you'll never notice. --- reply2 (18 votes) ---
Adding: the lab machines exist and are better than anything you'll buy. For the heavy assignments people just use those. --- reply 3 (12votes) ---
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.
```

**Chunk 4** — source: thread_office_hours_etiquette.txt#0 `` — produced by: chunker.py::split_documents``

```
THREAD: Is it weird to go to office hours with no specific question? --- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say. --- reply 2 (29 votes) ---
They're usually empty. You are doing the instructor a favour by turning up. --- reply 3 (18 votes) ---
```

**Chunk 5** — source: thread_professor_email.txt#0  `` — produced by: chunker.py::split_documents``

```
THREAD: Do professors actually answer email? --- reply 1 (21 votes) ---
Varies enormously. General rule I've found: if the syllabus states a response window, it's honoured. If it doesn't, assume 48 hours and don't panic before then. --- reply 2 (33 votes) ---
Office hours are dramatically more effective than email for anything that takes more than two sentences to answer. They're also usually empty. --- reply 3 (15 votes) ---
Empty office hours is the biggest unused resource here and I say that having wasted a year not going.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"What do students say about the best study spots on campus?"

**Answer:**

```
  (best distance 0.491, cutoff 0.7)

Based on the provided documents, students suggest the following study spots:
- Ridgeway Café before 10am, because it is empty, quiet, has good coffee, and they do not push you out (thread_study_spots.txt).
- The open lounges on floors 2 through 5 of the science building, which are unlocked and almost always empty (thread_study_spots.txt).
- The library third floor, if you need silence (thread_study_spots.txt).
- The group study rooms in the library, which can be booked by a single person to use alone since nobody checks (thread_study_spots.txt). 

Source: thread_study_spots.txt

Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_pass_fail.txt, thread_study_spots.txt

```

**My relevance cutoff:**

0.7

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| "What do students say about when to use the pass/fail option?" | Yes | 0.461 |
| "What should students pack for winter clothing?" | Yes | 0.626 |
| "What should a student do if they need to turn in an assignment late?" | Yes | 0.567 |
| "What do students say about the printing quota being enough?" | Yes | 0.591 |
| "What do students say about the best study spots on campus?" | Yes | 0.551 |
| "What is the capital of Mongolia?" | No | 0.825 |
| "How do I change the oil in a diesel engine?" | No | 0.934 |
| "Who won the 1994 World Cup?" | No | 0.886 |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.844 |
| "How do I write a for loop in Rust?" | No | 0.896 |

Each in-corpus question was run 3 times and returned the same best distance every time. Out-of-scope questions topped out at 0.825; in-corpus questions topped out at 0.626 — gate refused 5 of 5 out-of-scope questions. The midppoint of these two groups is around 0.7, that's why I picked 0.7 as my threshold.

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I used AI to help write my chunker.py split_documents dunction. I gave it instructions on what to implement based on my thoughts about splitting on sentences so that nothing is an incomplete thought. And also instructed it to follow the instructions in the document to create a proper function following the model of the fallback.
**2.**
I used Claude to help me decide what was the best threshold for the chunking based on the two groups of 5 sentence/questions each. I had started out with 0.5, then lowered it down to 0.4. But after analyzing the distances for the two groups, Claude suggested that a midpoint between them, 0.7, would be better and more appropriate. I took that into consideration and ended up keeping it as 0.7 because it balanced well with my chunk size and overlap numbers.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. Contain full sentences | 4 of 5 | | | | |
| 5. No more than 800 characters| 3 of 5 | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
