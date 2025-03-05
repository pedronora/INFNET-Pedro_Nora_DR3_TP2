def dfs_iterativo(grafo, ponto_inicial):
    """Executa a Busca em Profundidade (DFS) de forma iterativa."""
    contas_analisadas = set()
    pilha = [ponto_inicial]  # Lista usada como pilha (LIFO)

    print(f"Explorando as transações a partir de {ponto_inicial}:")
    while pilha:
        conta_atual = pilha.pop()  # Remove o último elemento da pilha
        if conta_atual not in contas_analisadas:
            print(conta_atual, end=" => ")
            contas_analisadas.add(conta_atual)

            for vizinho in reversed(grafo[conta_atual]):
                if vizinho == ponto_inicial:
                    print(vizinho)
                    return True
                # Reverso para seguir a mesma ordem da recursiva
                if vizinho not in contas_analisadas:
                    pilha.append(vizinho)

    print("Fim da exploração!")
    return False


if __name__ == "__main__":
    grafo1 = {
        "ContaA": ["ContaB"],
        "ContaB": ["ContaC"],
        "ContaC": ["ContaD"],
        "ContaD": [],
    }

    grafo2 = {
        "ContaA": ["ContaB"],
        "ContaB": ["ContaC"],
        "ContaC": ["ContaD"],
        "ContaD": ["ContaA"],
    }

    for n, item in enumerate([grafo1, grafo2]):
        resultado = dfs_iterativo(item, "ContaA")
        if resultado:
            print(f"Grafo{n+1} possui um ciclo!")
        else:
            print(f"Grafo{n+1} NÃO possui um ciclo!")
        print()
