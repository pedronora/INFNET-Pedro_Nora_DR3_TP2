from ex7 import grafo


def bfs(grafo, inicio):
    visitados = set()
    fila = [inicio]

    print(f"Ordem dos vértices visitados pela BFS a partir de {inicio}:")
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            print(vertice, end=" => ")
            visitados.add(vertice)
            fila.extend(grafo[vertice])
    print("Fim")


if __name__ == "__main__":
    bfs(grafo, "A")
