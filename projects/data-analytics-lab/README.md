# Data Analytics Lab — CO₂ Emissions

Projeto de análise de dados orientado a uma demanda real de Analytics: transformar uma base pública em indicadores reproduzíveis e conclusões documentadas.

## Pergunta

Como a emissão de CO₂ do Brasil evoluiu ao longo do tempo e como ela se compara ao cenário global?

## Fonte

Our World in Data — CO₂ dataset.

O script usa a fonte pública por padrão e aceita `--input` para execução offline/reprodutível com fixture local.

## Pipeline

1. Download da base
2. Seleção de Brasil e mundo
3. Tratamento e validação
4. Cálculo de indicadores
5. Exportação de dados para BI
6. Geração de gráfico
7. Registro das conclusões

## Stack

Python · Pandas · Matplotlib · Data Analysis

## Executar

```bash
pip install -r requirements.txt
python analysis.py
```

Para execução determinística sem internet:

```bash
python analysis.py --input data/sample_co2.csv
```

## Evidências

- [Resumo dos indicadores](output/summary.json)
- [Tabela do último ano](output/latest_indicators.csv)
- [Gráfico reproduzível](output/co2_trend.svg)
- [Descrição dos artefatos](output/README.md)

A execução validada com o fixture local reproduz os indicadores de 2024 usados nos artefatos.
