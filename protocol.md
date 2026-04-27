# MilBench Protocol v1.0 — Replication Guide

This document provides the complete procedure for conducting a MilBench evaluation at any professional military education institution. It covers panel composition, session logistics, AI preparation, examination conduct, grading, and post-examination data collection.

---

## 1. Panel Composition

Each examination panel consists of two to three faculty members. Panelists should meet the following criteria:

- Experience administering oral comprehensive examinations or thesis defenses (the USAWC pilot averaged 3.3 years of oral exam experience at the War College and 3.5 years at other institutions).
- Domain expertise spanning at least two of the institution's core academic disciplines (e.g., strategy, leadership, international relations, defense management, military operations, political science, law).
- Panelists should **not** have served as the AI system's "instructor" in any sense — no examiner should have fine-tuned, prompted, or otherwise prepared the AI before the examination.

Assemble a minimum of two panels. Three or more panels strengthen inter-rater reliability and enable cross-panel comparison. Each panel examines all AI models being tested to allow direct comparison within panels.

---

## 2. Model Selection

Select the AI models to be evaluated based on two requirements:

- **Conversational (voice) mode support.** MilBench is designed as an oral examination. Models must support real-time, multi-turn voice dialogue. Text-only models may be tested as a parallel track but should be reported separately, as modality affects performance.
- **Frontier-class capability.** MilBench evaluates the leading edge of commercial AI. Select the most capable generally available version of each model at the time of testing. Record exact model names and version numbers.

The USAWC pilot tested four models: ChatGPT 5.2, Gemini 3.1, Claude (Opus 4.6), and Grok 4.2. Future iterations should test whatever frontier models are current.

---

## 3. Examination Questions

Draw questions from the institution's own capstone examination slate. Requirements:

- Questions should demand multi-disciplinary integration across two or more courses in the curriculum.
- Questions should be open-ended and require sustained analysis, not factual recall.
- Use two to three questions per examination session, consistent with the institution's standard exam format.
- Faculty select questions from the slate as they would for a human student — AI models should not see the questions in advance.

**Regarding question release:** The USAWC rotates its examination slate annually. Questions from prior academic years may be published for replication purposes once they are no longer in active use. Current-year questions should never be published.

---

## 4. The Standardized Prompt

Before each examination, provide the AI model with a standardized prompt that establishes examination conditions. The prompt should:

- Identify the examination format, duration expectations, and the number of questions.
- Instruct the AI to respond as if it were a senior military officer sitting for an oral comprehensive examination.
- State that the AI has **not** been provided with any institutional syllabi, course readings, or preparatory materials.
- Instruct the AI not to use external search tools or web access during the examination.
- Set the expectation that initial responses should be approximately five minutes in length, followed by faculty follow-up questions and dialogue.

The exact prompt used in the USAWC pilot is in `prompts/exam-prompt.md`.

---

## 5. Examination Conduct

### Setup
- Conduct examinations in a quiet environment with stable internet connectivity.
- Use a single device per session (laptop or tablet with microphone/speaker) to interact with the AI model in conversational mode.
- Record all sessions (audio at minimum; video of the screen recommended) for transcript production and post-hoc analysis.
- Have blank rubric score sheets ready for each panelist.

### Session Flow
1. **Open the AI session.** Start a new conversation with the AI model. Deliver the standardized prompt.
2. **Ask the first question.** Read the question aloud as you would to a student.
3. **Allow the AI to respond.** Note the response duration. Do not interrupt unless the model misunderstands the question or exceeds a reasonable time limit (the USAWC pilot allowed responses up to 10 minutes before redirecting).
4. **Conduct follow-up questioning.** Faculty ask impromptu follow-up questions as they would with any student — probing for strategic-level theories, demanding historical or contemporary examples, challenging incomplete assertions, and pressing on weak points. Duration: approximately 10 minutes per question.
5. **Repeat** for the second and third questions.
6. **Conclude the session.** Total examination time will vary. The USAWC pilot ranged from 15 minutes to a full hour depending on the model. Do not artificially extend or truncate — let the examination run its natural course.

### Technical Issues
Document any technical anomalies:
- Voice degradation (pitch changes, garbled audio, robotic tone)
- Connectivity interruptions
- Model-initiated web searches despite prompt instructions
- Mid-response abandonment when interrupted
- Fabricated references or credentials

These are data points, not grounds for restarting the session. The USAWC pilot observed all of the above across different models.

---

## 6. Grading

### Independent Assessment
After the examination concludes, each panelist grades the AI independently before any deliberation, using the three rubric categories:

1. **Integration of Course Concepts** — see `rubric/integration.md`
2. **Strategic Thinking** — see `rubric/strategic-thinking.md`
3. **Communication** — see `rubric/communication.md`

Each category receives a letter grade. Record the independent grades before deliberation begins.

### Deliberation
Panelists then deliberate as they would for a student examination:
- Compare independent grades.
- Discuss specific strengths and weaknesses observed.
- Arrive at a consensus grade for each category (or record the range if consensus is not reached).
- Record deliberation notes — these are a primary data source.

### GPA Conversion
Convert letter grades to the institution's GPA scale. The USAWC uses a 4.333 scale:

| Letter Grade | GPA Value |
|---|---|
| A+ | 4.333 |
| A | 4.000 |
| A- | 3.667 |
| B+ | 3.333 |
| B | 3.000 |
| B- | 2.667 |
| C+ | 2.333 |

See `scoring/gpa-conversion.md` for the full conversion table and instructions for mapping to other institutional scales.

---

## 7. Post-Examination Survey

Administer the post-examination survey to each panelist after all AI models have been examined. The survey captures:

- Examiner background (years of oral exam experience, academic discipline, frequency of AI use)
- Pre-examination grade predictions versus actual outcomes
- Qualitative observations on each model's performance
- Comparative assessment: how did each AI model perform relative to graduating students?
- Examiner confidence in the rubric's ability to differentiate AI from human performance

The full survey instruments are in `survey/pre-exam-survey.md` and `survey/post-exam-survey.md`.

---

## 8. Statistical Analysis

With grades from multiple panels and models, conduct the following:

- **Descriptive statistics** — mean GPA, standard deviation, and range per model.
- **One-way ANOVA** — test whether mean GPA differences across models are statistically significant.
- **Post-hoc pairwise comparisons** — identify which specific model pairs differ significantly (Tukey HSD or equivalent).
- **Effect sizes** — report η² (eta-squared) for the overall ANOVA and Cohen's d for pairwise comparisons.

A Python script implementing this analysis is in `scoring/analysis.py`. It accepts a CSV of raw grades and produces the summary statistics, ANOVA table, and pairwise comparison results.

Minimum sample: the USAWC pilot produced 57 individual category scores across four models and three panels. Larger samples from more panels or more examination rounds will increase statistical power.

---

## 9. Reporting Results

When reporting MilBench results, include at minimum:

- Institution name and examination format
- Models tested (exact names and version numbers)
- Number of panels, panelists, and examination rounds
- The standardized prompt used
- Mean GPA, SD, and range per model
- ANOVA results (F statistic, degrees of freedom, p-value, η²)
- Post-hoc comparison results
- Summary of qualitative observations from faculty deliberations
- Any technical anomalies observed

Submit replication data to the MilBench repository via pull request or contact the authors directly.

---

## 10. Known Limitations

The following limitations apply to any MilBench replication and should be reported alongside results:

- **Sample size.** Small panel counts limit statistical power. Plan for a minimum of three panels.
- **Rater bias.** All examiners know they are evaluating AI. A blinded methodology (anonymized transcripts evaluated without knowledge of the source) would reduce this uncertainty and is recommended for future iterations.
- **No curriculum access.** The baseline protocol deliberately withholds institutional course materials from AI models. Replication with curriculum-primed models is a separate experimental condition and should be reported as such.
- **Conversational mode constraints.** Voice interaction introduces variables (connectivity, audio quality, interruption handling) absent from text-based evaluation. Document all technical issues.
- **Question selection effects.** Faculty choose which questions to ask from the slate, introducing a selection variable. Standardizing question assignment across models (same questions for all models within a panel) strengthens comparability.
