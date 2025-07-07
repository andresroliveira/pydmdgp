from pydmdgp import Graph, solve

INSTANCE_PATH = "data/instance.csv"


def main():
    print("Running the solver...")
    print(f"Carregando a instância do arquivo: {INSTANCE_PATH}")

    graph = Graph.from_csv(INSTANCE_PATH)
    X = solve(graph)

    for i in range(1, graph.n + 1):
        print(f"Átomo {i}: {X[i]}")


if __name__ == "__main__":
    main()
