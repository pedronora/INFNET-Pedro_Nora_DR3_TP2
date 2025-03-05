from ex4 import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    centros = ["A", "B", "C", "D", "E"]
    conexoes = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")]

    for centro in centros:
        grafo.adicionar_vertice(centro)

    for conexao in conexoes:
        grafo.adicionar_aresta(conexao[0], conexao[1])

    for centro in centros:
        grafo.mostrar_vizinhos(centro)
