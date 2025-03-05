grafo = {
    "Bairro A": ["Bairro B", "Bairro C", "Bairro D", "Bairro E"],
    "Bairro B": ["Bairro A", "Bairro F"],
    "Bairro C": ["Bairro A", "Bairro D"],
    "Bairro D": ["Bairro A", "Bairro C", "Bairro E"],
    "Bairro E": ["Bairro A", "Bairro D", "Bairro F"],
    "Bairro F": ["Bairro B", "Bairro E"],
}


def mostrar_grafo(grafo):
    for vertice in grafo:
        print(f"{vertice}: {', '.join(grafo[vertice])}")


if __name__ == "__main__":
    mostrar_grafo(grafo)
