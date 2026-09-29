# RAG & LLM Engineering

Projeto técnico de Retrieval-Augmented Generation com arquitetura modular e foco em rastreabilidade.

## Objetivo

Demonstrar o fluxo fundamental de um sistema RAG sem esconder a parte importante atrás de um framework:

`documentos → representação vetorial → recuperação → contexto → resposta`

A primeira versão usa TF-IDF para tornar a recuperação local, reproduzível e fácil de inspecionar. A arquitetura pode ser evoluída para embeddings e banco vetorial.

## Stack

Python · scikit-learn · RAG · NLP

## Executar

```bash
pip install -r requirements.txt
python rag.py
```

Depois faça uma pergunta no terminal.

## Evidências

- [Avaliação do smoke test](output/evaluation.json)
- [Demonstração documentada](output/demo.md)

O teste de referência recuperou contexto com score máximo de similaridade **0.568** para a consulta usada no smoke test.

## Por que começar sem um LLM?

Porque RAG não é apenas "chamar um modelo". Primeiro precisamos conseguir observar e avaliar a recuperação de contexto. Depois podemos trocar o gerador por um LLM via API sem alterar a camada de retrieval.
