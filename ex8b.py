def dfs_iterativo_melhorado(grafo, ponto_inicial, instituicoes):
    """Executa a DFS de forma iterativa, priorizando transações entre múltiplas instituições."""
    contas_analisadas = set()
    pilha = [(ponto_inicial, instituicoes[ponto_inicial])]

    print(f"Explorando as transações a partir de {ponto_inicial}:")
    while pilha:
        conta_atual, instituicao_atual = pilha.pop()
        if conta_atual not in contas_analisadas:
            print(f"{conta_atual} ({instituicao_atual})", end=" => ")
            contas_analisadas.add(conta_atual)

            for vizinho in reversed(grafo[conta_atual]):
                instituicao_vizinho = instituicoes[vizinho]
                if (
                    vizinho == ponto_inicial
                    and instituicao_vizinho != instituicao_atual
                ):
                    print(f"{vizinho} ({instituicao_vizinho})")
                    return True
                if vizinho not in contas_analisadas:
                    pilha.append((vizinho, instituicao_vizinho))

    print("Fim da exploração!")
    return False


if __name__ == "__main__":
    grafo1 = {
        "ContaA": ["ContaB"],
        "ContaB": ["ContaC"],
        "ContaC": ["ContaD"],
        "ContaD": ["ContaA"],
    }

    instituicoes1 = {
        "ContaA": "BancoX",
        "ContaB": "BancoY",
        "ContaC": "BancoZ",
        "ContaD": "BancoW",
    }

    grafo2 = {
        "ContaA": ["ContaB"],
        "ContaB": ["ContaC"],
        "ContaC": ["ContaD"],
        "ContaD": [],
    }

    instituicoes2 = {
        "ContaA": "BancoX",
        "ContaB": "BancoY",
        "ContaC": "BancoZ",
        "ContaD": "BancoW",
    }

    print("=== Teste 1: Grafo com ciclo ===")
    resultado1 = dfs_iterativo_melhorado(grafo1, "ContaA", instituicoes1)
    if resultado1:
        print("Ciclo suspeito detectado!")
    else:
        print("Nenhum ciclo suspeito detectado.")
    print()

    print("=== Teste 2: Grafo sem ciclo ===")
    resultado2 = dfs_iterativo_melhorado(grafo2, "ContaA", instituicoes2)
    if resultado2:
        print("Ciclo suspeito detectado! Priorizar")
    else:
        print("Nenhum ciclo suspeito detectado.")
