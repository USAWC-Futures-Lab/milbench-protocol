# MilBench Protocol v1.0

**A domain-specific benchmark for evaluating commercial AI systems against senior military education standards.**

MilBench uses the US Army War College (USAWC) oral comprehensive examination framework to benchmark commercial AI systems on strategic thinking, integration of military concepts, and communication. Unlike general-purpose AI benchmarks (MMLU, ARC, HumanEval), MilBench applies a real-world, dialogue-based assessment designed and administered by experienced faculty evaluators.

The pilot ran from February to March 2026 at the USAWC Center for Strategic Leadership, Carlisle Barracks, Pennsylvania. Three faculty panels examined four frontier AI models (ChatGPT 5.2, Gemini 3.1, Claude 4.6, and Grok 4.2) using the same protocols, questions, and rubrics applied to graduating senior military officers. All four models passed. Results and analysis are published in *Parameters*.

This repository provides everything a professional military education institution needs to replicate MilBench at its own institution with its own faculty and examination standards.

---

## Repository Contents

```
milbench-protocol/
├── README.md                  # This file — overview, purpose, citation
├── protocol.md                # Step-by-step replication guide
├── catechism/
│   └── index.html             # MilBench Catechism — AI interrogation training tool
├── prompts/
│   └── exam-prompt.md         # Standardized prompt and script for AI examinees
├── rubric/
│   ├── integration.md         # Rubric 1: Integration of Course Concepts
│   ├── strategic-thinking.md  # Rubric 2: Strategic Thinking
│   └── communication.md       # Rubric 3: Communication
├── survey/
│   ├── pre-exam-survey.md     # Pre-examination examiner survey
│   └── post-exam-survey.md    # Post-examination examiner survey
├── scoring/
│   ├── gpa-conversion.md      # Letter grade to GPA conversion table
│   └── analysis.py            # Statistical analysis script (ANOVA, post-hoc, effect sizes)
└── questions/
    └── README.md              # Note on question availability and rotation
```

---

## What MilBench Measures

MilBench evaluates AI performance across three equally weighted rubric categories drawn from the USAWC oral comprehensive examination:

1. **Integration of Course Concepts** — Can the system synthesize material across multiple disciplines (strategy, leadership, defense management, regional studies) into a coherent response?

2. **Strategic Thinking** — Does the system demonstrate creative, systems, ethical, and historical thinking while acknowledging competing viewpoints?

3. **Communication** — Does the system organize complex ideas clearly, declare frames of reference, and incorporate relevant examples?

Each category is graded on a four-tier scale: Outstanding, Superior, Performed to Standard, and Unsatisfactory. A passing score requires a B or higher in all three categories.

The multi-turn, conversational format — with impromptu faculty follow-up questions — tests depth of reasoning under sustained pressure, not single-turn recall.

---

## What MilBench Does Not Measure

MilBench assesses whether AI systems can demonstrate strategic knowledge at the level the oral examination measures. It does not assess judgment, accountability, or the capacity to act under genuine uncertainty with real consequences. The distinction between intelligence (command over frameworks, vocabulary, and precedent) and wisdom (the capacity to weigh incommensurable values under uncertainty) remains central to interpreting results.

---

## Who Can Run MilBench

Any institution with the following can replicate the protocol:

- **Faculty evaluators** experienced in oral examination or thesis defense formats, with domain expertise in strategy, military operations, international relations, leadership, or related fields.
- **An examination question slate** drawn from the institution's own curriculum. MilBench does not require USAWC-specific questions — the protocol is designed to accept any institution's capstone examination content.
- **Access to frontier AI models** that support conversational (voice) mode. The pilot tested four models; replication can use any combination of current commercial systems.
- **The rubric instruments and survey tools** provided in this repository, adapted as needed to the institution's grading standards.

Senior service colleges, command and staff colleges, joint PME institutions, and allied military education programs are all viable replication sites. Civilian institutions with oral comprehensive examination traditions (doctoral programs, professional credentialing bodies) can also adapt the protocol.

---

## Adapting MilBench to Your Institution

MilBench was designed at the USAWC but is not locked to its curriculum. To replicate at another institution:

1. **Substitute your own questions.** Replace the USAWC examination slate with your institution's capstone questions. The protocol works with any set of questions that require multi-disciplinary integration and sustained faculty dialogue.

2. **Adapt the rubrics.** The three-category rubric structure (integration, thinking, communication) is broadly applicable, but the descriptors should reflect your institution's learning outcomes. The rubric files in this repository are templates — modify the language to match your standards.

3. **Calibrate your grading scale.** The USAWC uses a 4.333 GPA scale. The scoring directory includes the conversion table and a script that accepts any institutional scale as input.

4. **Run the examiner surveys.** The pre- and post-examination surveys capture examiner expertise, expectations, and observations. These are essential for controlling rater bias and comparing results across institutions.

---

## Pilot Results Summary

| Model | Mean GPA | SD | Range | Grade | n |
|---|---|---|---|---|---|
| ChatGPT 5.2 | 3.38 | 0.27 | 2.67–3.67 | B+ | 15 |
| Gemini 3.1 | 3.28 | 0.26 | 3.00–3.67 | B+ | 13 |
| Claude 4.6 | 3.98 | 0.32 | 3.33–4.33 | A | 16 |
| Grok 4.2 | 3.38 | 0.29 | 3.00–3.67 | B+ | 13 |

One-way ANOVA: F(3, 54) = 17.90, p < .001, η² = .499. Post-hoc comparisons showed Claude differed significantly from each of the other three models (all p < .001), while ChatGPT, Grok, and Gemini were statistically indistinguishable (all p > .35).

Full analysis is in the published paper.

---

## MilBench Catechism — Master the Art of the Question

MilBench established that commercial AI systems can pass the War College capstone assessment. Catechism trains the skill that matters next: evaluating whether AI-generated analysis is trustworthy.

Students receive an AI-generated staff product — a theater assessment, campaign critique, or policy recommendation — containing embedded analytical flaws: fabricated references, unsupported assertions, anchoring bias, missing perspectives, and doctrinal errors. Their job is to interrogate the analyst who wrote it, find what's wrong, and push back until the analysis breaks.

The AI analyst behaves the way MilBench models did: defends initially, yields under pressure, avoids naming adversaries until pressed. Every scenario is generated fresh — no two sessions are identical.

**[Try it live →](https://usawc-milbench-catechism.netlify.app/)**

To self-host, download [`catechism/index.html`](catechism/index.html) and open it in a browser. You will need your own [Anthropic API key](https://console.anthropic.com/).

---

## Citation

If you use MilBench in your research or institutional assessment, cite the original study:

> Boyce, Kevin M., John A. Nagl, and Kristan J. Wheaton. "Can AI Pass the US Army War College?" *Parameters* (2026).

If you use the protocol materials from this repository:

> MilBench Protocol v1.0. Center for Strategic Leadership, US Army War College, 2026. https://github.com/USAWC-Futures-Lab/milbench-protocol

---

## Contributing

MilBench improves through replication. If your institution runs a MilBench iteration, we encourage you to:

- Share your adapted rubrics and question structure (not the questions themselves, if still in rotation).
- Report aggregate results for cross-institutional comparison.
- Submit issues or pull requests to improve the protocol documentation.

Contact: Kevin M. Boyce, Center for Strategic Leadership, US Army War College

---

## License

CC0-1.0 for the protocol documents. MIT for code in the scoring directory and catechism tool.

---

## Authors

- **Kevin M. Boyce** — Director, Futures Lab, Center for Strategic Leadership, USAWC
- **John A. Nagl** — General John J. Pershing Professor of Warfighting Studies, USAWC
- **Kristan J. Wheaton** — Professor of Strategic Futures, USAWC
