# GPA Conversion Table

## USAWC 4.333 Scale

The US Army War College uses a 4.333-point GPA scale. This is the scale used in the MilBench pilot. All published MilBench results use this scale for comparability.

| Letter Grade | Percentage | GPA Value |
|---|---|---|
| A+ | 97–100 | 4.333 |
| A | 94–96 | 4.000 |
| A- | 90–93 | 3.667 |
| B+ | 87–89 | 3.333 |
| B | 84–86 | 3.000 |
| B- | 80–83 | 2.667 |
| C+ | 77–79 | 2.333 |
| C | 74–76 | 2.000 |
| C- | 70–73 | 1.667 |

**Passing threshold:** B (3.000) or higher in all three rubric categories.

## Adapting to Other Scales

If your institution uses a different GPA scale (e.g., 4.0), map your letter grades to your own scale and report results on that scale. Include the conversion table in your replication report so cross-institutional comparisons can be normalized.

The `analysis.py` script accepts a `--scale` parameter to adjust the GPA mapping.

## Recording Grades

Record grades in a CSV file with the following columns:

```
panel,model,version,round,examiner,integration,strategic_thinking,communication
A,Claude,4.6,1,Examiner1,A,A,A-
A,ChatGPT,5.2,1,Examiner1,B+,B+,B
...
```

Each row represents one examiner's independent grades for one model in one examination round. The analysis script converts letter grades to GPA values automatically.
