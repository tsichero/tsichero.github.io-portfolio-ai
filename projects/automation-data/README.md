# Automated Data Report

Pipeline de automação que lê uma planilha, valida os dados, calcula indicadores e gera um relatório HTML.

## Fluxo

`input/sales.xlsx → validação → tratamento → KPIs → relatório.html`

## Stack

Python · Pandas · OpenPyXL · HTML

## Executar

```bash
pip install -r requirements.txt
python generate_report.py
```

Se não existir uma planilha em `input/sales.xlsx`, o projeto cria uma pequena base de demonstração para permitir execução imediata.

## Indicadores

- faturamento total
- ticket médio
- quantidade de pedidos
- faturamento por categoria
- faturamento por região

## Evidências

- [Relatório HTML](output/report.html)
- [Faturamento por categoria](output/revenue_by_category.csv)
- [Faturamento por região](output/revenue_by_region.csv)

Resultado validado da demonstração: **5 pedidos · R$ 17.850,00 de faturamento · R$ 3.570,00 de ticket médio**.

O objetivo é demonstrar automação reproduzível, e não apenas uma análise feita manualmente uma vez.
