from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCS = Path(__file__).parent / "documents"
documents = [
    p.read_text(encoding="utf-8")
    for p in sorted(DOCS.glob("*.txt"))
]

if not documents:
    raise RuntimeError("Nenhum documento encontrado em documents/")

vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2))
matrix = vectorizer.fit_transform(documents)


def retrieve(query: str, top_k: int = 2):
    q = vectorizer.transform([query])
    scores = cosine_similarity(q, matrix).ravel()
    indexes = scores.argsort()[::-1][:top_k]
    return [(int(i), float(scores[i]), documents[i]) for i in indexes]


def main():
    print("RAG Lab — digite 'sair' para encerrar.")
    while True:
        query = input("\nPergunta: ").strip()
        if query.lower() == "sair":
            break

        results = retrieve(query)
        print("\nContexto recuperado:")
        for i, score, text in results:
            print(f"\n[{i}] score={score:.3f}\n{text[:500]}")


if __name__ == "__main__":
    main()
