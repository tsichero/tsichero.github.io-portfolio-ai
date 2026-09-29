from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
INPUT = BASE / "input" / "sales.xlsx"
OUTPUT = BASE / "output"
OUTPUT.mkdir(exist_ok=True)
INPUT.parent.mkdir(exist_ok=True)

if not INPUT.exists():
    demo = pd.DataFrame([
        ["2026-01-03", "SP", "Software", 2, 1200.0],
        ["2026-01-07", "RJ", "Consultoria", 1, 2500.0],
        ["2026-02-11", "SP", "Consultoria", 2, 3000.0],
        ["2026-02-19", "MG", "Treinamento", 3, 850.0],
        ["2026-03-05", "PR", "Software", 4, 1100.0],
    ], columns=["date", "region", "category", "quantity", "unit_price"])
    demo.to_excel(INPUT, index=False)

df = pd.read_excel(INPUT)
required = {"date", "region", "category", "quantity", "unit_price"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Colunas ausentes: {sorted(missing)}")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
df = df.dropna(subset=list(required))
df["revenue"] = df["quantity"] * df["unit_price"]

total_revenue = df["revenue"].sum()
orders = len(df)
avg_ticket = total_revenue / orders if orders else 0

by_category = (
    df.groupby("category", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

by_region = (
    df.groupby("region", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Automated Data Report</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; line-height: 1.5; }}
.kpis {{ display:flex; gap:20px; flex-wrap:wrap; }}
.kpi {{ padding:20px; border:1px solid #ddd; border-radius:12px; min-width:180px; }}
</style>
</head>
<body>
<h1>Relatório automatizado</h1>
<div class="kpis">
<div class="kpi"><strong>Faturamento</strong><br>R$ {total_revenue:,.2f}</div>
<div class="kpi"><strong>Pedidos</strong><br>{orders}</div>
<div class="kpi"><strong>Ticket médio</strong><br>R$ {avg_ticket:,.2f}</div>
</div>
<h2>Por categoria</h2>
{by_category.to_html(index=False)}
<h2>Por região</h2>
{by_region.to_html(index=False)}
</body>
</html>"""

(OUTPUT / "report.html").write_text(html, encoding="utf-8")
by_category.to_csv(OUTPUT / "revenue_by_category.csv", index=False)
by_region.to_csv(OUTPUT / "revenue_by_region.csv", index=False)

print(f"Relatório criado em {OUTPUT / 'report.html'}")
