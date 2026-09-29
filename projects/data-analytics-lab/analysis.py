"""Reproducible CO₂ analytics pipeline.

Default source: Our World in Data CO₂ dataset.
For deterministic CI/local execution, pass a local CSV with --input.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
REQUIRED_COLUMNS = {"country", "year", "co2", "population"}


def load_data(source: str | Path | None = None) -> pd.DataFrame:
    """Load and validate the minimum fields required by the analysis."""
    df = pd.read_csv(source or DATA_URL)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = df.copy()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["co2"] = pd.to_numeric(df["co2"], errors="coerce")
    df["population"] = pd.to_numeric(df["population"], errors="coerce")
    df = df.dropna(subset=["country", "year", "co2", "population"])

    if (df["population"] <= 0).any():
        raise ValueError("Population must be greater than zero.")
    if (df["co2"] < 0).any():
        raise ValueError("CO₂ values must be non-negative for this analysis.")

    df["year"] = df["year"].astype(int)
    df["co2_per_capita"] = df["co2"] * 1_000_000 / df["population"]
    return df


def build_summary(subset: pd.DataFrame) -> dict:
    """Create decision-ready indicators for the latest available year."""
    brazil = subset[subset["country"] == "Brazil"].sort_values("year")
    latest_year = int(subset["year"].max())
    latest = subset[subset["year"] == latest_year]

    if brazil.empty:
        raise ValueError("Brazil is not available in the selected dataset.")

    start = brazil.iloc[0]
    end = brazil.iloc[-1]
    previous = brazil.iloc[-2] if len(brazil) > 1 else None

    summary = {
        "latest_year": latest_year,
        "brazil_co2_mt": round(float(end["co2"]), 3),
        "brazil_co2_per_capita_t": round(float(end["co2_per_capita"]), 3),
        "brazil_first_year": int(start["year"]),
        "brazil_first_co2_mt": round(float(start["co2"]), 3),
        "brazil_last_year": int(end["year"]),
        "brazil_last_co2_mt": round(float(end["co2"]), 3),
        "records_analyzed": int(len(subset)),
    }

    if previous is not None:
        summary["brazil_yoy_change_pct"] = round(
            (float(end["co2"]) / float(previous["co2"]) - 1) * 100, 2
        )

    return summary


def run_pipeline(source: str | Path | None, output_dir: str | Path = "output") -> dict:
    """Run the complete pipeline and persist machine-readable evidence."""
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    df = load_data(source)
    subset = df[df["country"].isin(["Brazil", "World"])].copy()

    if subset.empty:
        raise ValueError("No Brazil/World records found.")

    latest_year = int(subset["year"].max())
    latest = subset[subset["year"] == latest_year].copy()
    latest.to_csv(output / "latest_indicators.csv", index=False)

    summary = build_summary(subset)
    summary["source"] = str(source) if source else DATA_URL
    summary["source_type"] = "local_fixture" if source else "public_dataset"

    with (output / "summary.json").open("w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=2)

    plt.figure(figsize=(10, 5))
    for country in ["Brazil", "World"]:
        part = subset[subset["country"] == country].sort_values("year")
        plt.plot(part["year"], part["co2"], label=country)

    plt.title("CO₂ emissions — Brazil vs World")
    plt.xlabel("Year")
    plt.ylabel("CO₂ emissions (million tonnes)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output / "co2_trend.png", dpi=160)
    plt.savefig(output / "co2_trend.svg")
    plt.close()

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the CO₂ analytics pipeline.")
    parser.add_argument(
        "--input",
        help="Optional local CSV for deterministic/offline execution.",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for generated evidence.",
    )
    args = parser.parse_args()

    summary = run_pipeline(args.input, args.output_dir)
    print(f"Latest year: {summary['latest_year']}")
    print(f"Brazil CO₂: {summary['brazil_co2_mt']:.2f} Mt")
    print(f"Brazil CO₂ per capita: {summary['brazil_co2_per_capita_t']:.2f} t/person")


if __name__ == "__main__":
    main()
