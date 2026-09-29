# Data Analytics Lab — CO₂ Emissions

Projeto de análise de dados orientado a uma demanda real de Analytics: transformar uma base pública em indicadores reproduzíveis e conclusões documentadas.

## Pergunta

Como a emissão de CO₂ do Brasil evoluiu ao longo do tempo e como ela se compara ao cenário global?

## Fonte

Our World in Data — CO₂ dataset:
https://github.com/owid/co2-data

O projeto baixa a base diretamente no script para manter o processo reproduzível.

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

## Como executar

```bash
pip install -r requirements.txt
python analysis.py
```

Os resultados são gravados em `output/`.

## Evidência

O projeto não depende de uma análise manual: o mesmo comando reconstrói os dados derivados e os indicadores.
