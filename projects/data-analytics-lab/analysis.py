from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
import argparse

DATA_URL = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
OUTPUT = Path("output")

parser = argparse.ArgumentParser(description="Run CO2 analytics pipeline")
parser.add_argument("--input", help="Optional local CSV for reproducible/offline execution")
args = parser.parse_args()
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(args.input if args.input else DATA_URL)

required = {"country", "year", "co2", "population"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Colunas ausentes: {sorted(missing)}")

subset = df[df["country"].isin(["Brazil", "World"])].copy()
subset = subset.dropna(subset=["co2", "population"])
subset["co2_per_capita"] = subset["co2"] * 1_000_000 / subset["population"]

latest_year = int(subset["year"].max())
latest = subset[subset["year"] == latest_year].copy()

latest.to_csv(OUTPUT / "latest_indicators.csv", index=False)

brazil = subset[subset["country"] == "Brazil"].sort_values("year")
start = brazil.iloc[0]
end = brazil.iloc[-1]

summary = {
    "latest_year": latest_year,
    "brazil_co2_mt": float(end["co2"]),
    "brazil_co2_per_capita_t": float(end["co2_per_capita"]),
    "brazil_first_year": int(start["year"]),
    "brazil_first_co2_mt": float(start["co2"]),
    "brazil_last_year": int(end["year"]),
    "brazil_last_co2_mt": float(end["co2"]),
}

with open(OUTPUT / "summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

plt.figure(figsize=(10, 5))
for country in ["Brazil", "World"]:
    part = subset[subset["country"] == country]
    plt.plot(part["year"], part["co2"], label=country)

plt.title("CO₂ emissions — Brazil vs World")
plt.xlabel("Year")
plt.ylabel("CO₂ emissions (million tonnes)")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT / "co2_trend.png", dpi=160)
plt.close()

print(f"Latest year: {latest_year}")
print(f"Brazil CO₂: {end['co2']:.2f} Mt")
print(f"Brazil CO₂ per capita: {end['co2_per_capita']:.2f} t/person")
