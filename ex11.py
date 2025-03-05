class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()

        print(vertice, end=" ")
        visitados.add(vertice)

        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)


if __name__ == "__main__":
    vertices = ["A", "B", "C", "D", "E"]
    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")]

    grafo = Grafo()

    for vertice in vertices:
        grafo.adicionar_vertice(vertice)

    for aresta in arestas:
        grafo.adicionar_aresta(aresta[0], aresta[1])

    print("Busca em Profundidade (DFS) a partir de 'A':")
    grafo.dfs_recursivo("A")
    print()
