# Automated Data Report

Pipeline de automação que lê uma planilha, valida os dados, calcula indicadores e gera um relatório HTML.

## Fluxo

`input.xlsx → validação → tratamento → KPIs → relatório.html`

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

O objetivo é demonstrar automação reproduzível, e não apenas uma análise feita manualmente uma vez.
