class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo"""
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso=1):
        """Adiciona uma aresta entre dois vértices"""
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append((vertice2, peso))
            self.lista_adjacencia[vertice2].append((vertice1, peso))

    def mostrar_grafo(self):
        """Exibe o grafo na forma de lista de adjacência"""
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        """Exibe os vizinhos de um determinado vértice"""
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs_menor_caminho(self, inicio, destino):
        """Retorna o caminho mais curto entre dois centros usando BFS"""
        fila = [(inicio, [inicio])]
        visitados = set()

        while fila:
            atual, caminho = fila.pop(0)
            if atual == destino:
                return caminho

            if atual not in visitados:
                visitados.add(atual)
                for vizinho, _ in self.lista_adjacencia.get(atual, []):
                    if vizinho not in visitados:
                        fila.append((vizinho, caminho + [vizinho]))

        return None


if __name__ == "__main__":
    grafo = Grafo()

    centros = ["A", "B", "C", "D", "E"]
    conexoes = [
        ("A", "B", 3),
        ("A", "C", 2),
        ("B", "D", 4),
        ("C", "E", 5),
        ("D", "E", 1),
    ]

    for centro in centros:
        grafo.adicionar_vertice(centro)

    for aresta in conexoes:
        grafo.adicionar_aresta(aresta[0], aresta[1], aresta[2])

    print(
        f"Menor caminho entre 'A' e 'E': {', '.join(grafo.bfs_menor_caminho("A", "E"))}"
    )
