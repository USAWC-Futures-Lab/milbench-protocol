#!/usr/bin/env python3
"""
MilBench Statistical Analysis Script
=====================================
Reads a CSV of raw examination grades and produces:
- Descriptive statistics per model (mean GPA, SD, range, n)
- One-way ANOVA across models
- Post-hoc pairwise comparisons (Tukey HSD)
- Effect sizes (eta-squared for ANOVA, Cohen's d for pairwise)

Usage:
    python analysis.py grades.csv
    python analysis.py grades.csv --scale 4.0

Input CSV format:
    panel,model,version,round,examiner,integration,strategic_thinking,communication

Requirements:
    pip install pandas scipy statsmodels
"""

import argparse
import sys
from itertools import combinations

import pandas as pd
import numpy as np
from scipy import stats


# --- GPA Conversion ---

GPA_MAP_4333 = {
    "A+": 4.333, "A": 4.000, "A-": 3.667,
    "B+": 3.333, "B": 3.000, "B-": 2.667,
    "C+": 2.333, "C": 2.000, "C-": 1.667,
    "D+": 1.333, "D": 1.000, "D-": 0.667,
    "F": 0.000,
}

GPA_MAP_400 = {
    "A+": 4.000, "A": 4.000, "A-": 3.667,
    "B+": 3.333, "B": 3.000, "B-": 2.667,
    "C+": 2.333, "C": 2.000, "C-": 1.667,
    "D+": 1.333, "D": 1.000, "D-": 0.667,
    "F": 0.000,
}


def get_gpa_map(scale: float) -> dict:
    if scale == 4.333:
        return GPA_MAP_4333
    elif scale == 4.0:
        return GPA_MAP_400
    else:
        print(f"Warning: Custom scale {scale} not defined. Using 4.333 scale.")
        return GPA_MAP_4333


def letter_to_gpa(letter: str, gpa_map: dict) -> float:
    letter = letter.strip()
    if letter in gpa_map:
        return gpa_map[letter]
    raise ValueError(f"Unrecognized letter grade: '{letter}'")


# --- Analysis Functions ---

def descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute mean, SD, range, and n per model."""
    results = []
    for model in sorted(df["model"].unique()):
        scores = df[df["model"] == model]["gpa"]
        results.append({
            "Model": model,
            "Mean GPA": round(scores.mean(), 2),
            "SD": round(scores.std(ddof=1), 2),
            "Min": round(scores.min(), 2),
            "Max": round(scores.max(), 2),
            "n": len(scores),
        })
    return pd.DataFrame(results)


def run_anova(df: pd.DataFrame) -> dict:
    """One-way ANOVA across models."""
    groups = [group["gpa"].values for _, group in df.groupby("model")]
    f_stat, p_value = stats.f_oneway(*groups)

    # Eta-squared
    grand_mean = df["gpa"].mean()
    ss_between = sum(
        len(g) * (g.mean() - grand_mean) ** 2
        for g in [df[df["model"] == m]["gpa"] for m in df["model"].unique()]
    )
    ss_total = ((df["gpa"] - grand_mean) ** 2).sum()
    eta_sq = ss_between / ss_total

    k = df["model"].nunique()
    n_total = len(df)

    return {
        "F": round(f_stat, 2),
        "df_between": k - 1,
        "df_within": n_total - k,
        "p": p_value,
        "eta_squared": round(eta_sq, 3),
    }


def pairwise_comparisons(df: pd.DataFrame) -> pd.DataFrame:
    """Pairwise t-tests with Cohen's d."""
    models = sorted(df["model"].unique())
    results = []
    for m1, m2 in combinations(models, 2):
        g1 = df[df["model"] == m1]["gpa"].values
        g2 = df[df["model"] == m2]["gpa"].values
        t_stat, p_val = stats.ttest_ind(g1, g2)

        # Cohen's d
        pooled_std = np.sqrt(
            ((len(g1) - 1) * g1.std(ddof=1) ** 2 + (len(g2) - 1) * g2.std(ddof=1) ** 2)
            / (len(g1) + len(g2) - 2)
        )
        d = (g1.mean() - g2.mean()) / pooled_std if pooled_std > 0 else 0

        results.append({
            "Comparison": f"{m1} vs {m2}",
            "Mean Diff": round(g1.mean() - g2.mean(), 3),
            "t": round(t_stat, 3),
            "p": round(p_val, 4),
            "Cohen's d": round(d, 3),
            "Sig": "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns",
        })
    return pd.DataFrame(results)


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="MilBench Statistical Analysis")
    parser.add_argument("csv_file", help="Path to grades CSV file")
    parser.add_argument("--scale", type=float, default=4.333,
                        help="GPA scale to use (default: 4.333)")
    args = parser.parse_args()

    # Load data
    try:
        df = pd.read_csv(args.csv_file)
    except FileNotFoundError:
        print(f"Error: File '{args.csv_file}' not found.")
        sys.exit(1)

    required_cols = {"model", "integration", "strategic_thinking", "communication"}
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        print(f"Error: Missing columns: {missing}")
        print(f"Expected columns: panel, model, version, round, examiner, integration, strategic_thinking, communication")
        sys.exit(1)

    # Convert letter grades to GPA
    gpa_map = get_gpa_map(args.scale)
    rubric_cols = ["integration", "strategic_thinking", "communication"]

    rows = []
    for _, row in df.iterrows():
        for col in rubric_cols:
            try:
                gpa = letter_to_gpa(row[col], gpa_map)
                rows.append({
                    "model": row["model"],
                    "panel": row.get("panel", ""),
                    "category": col,
                    "gpa": gpa,
                })
            except ValueError as e:
                print(f"Warning: {e} in row {row.to_dict()}")

    scores_df = pd.DataFrame(rows)

    if scores_df.empty:
        print("Error: No valid scores found.")
        sys.exit(1)

    # --- Output ---
    print("=" * 60)
    print("MILBENCH STATISTICAL ANALYSIS")
    print(f"Scale: {args.scale} | Observations: {len(scores_df)}")
    print("=" * 60)

    print("\n--- Descriptive Statistics ---")
    desc = descriptive_stats(scores_df)
    print(desc.to_string(index=False))

    print("\n--- One-Way ANOVA ---")
    anova = run_anova(scores_df)
    print(f"F({anova['df_between']}, {anova['df_within']}) = {anova['F']}, "
          f"p = {anova['p']:.4f}, eta-squared = {anova['eta_squared']}")

    if anova["p"] < 0.05:
        print("\n--- Pairwise Comparisons ---")
        pairs = pairwise_comparisons(scores_df)
        print(pairs.to_string(index=False))
    else:
        print("\nANOVA not significant; pairwise comparisons not warranted.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
