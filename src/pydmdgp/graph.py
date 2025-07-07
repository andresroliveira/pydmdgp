import pandas as pd
import numpy as np


class Graph:

    def __init__(self, n: int, distance_matrix: np.ndarray, adjacencies: dict,
                 edges: list[tuple[int, int, float]]):
        self.n = n
        self.distance_matrix = distance_matrix
        self.adjacencies = adjacencies
        self.edges = edges

    @classmethod
    def from_csv(cls, filepath: str):
        """Lê um grafo a partir de um arquivo CSV com colunas u, v, distance."""
        instance = pd.read_csv(filepath)
        n = max(instance.u.max(), instance.v.max())

        # Use NumPy para a matriz de distância
        distance_matrix = np.zeros((n + 1, n + 1), dtype=np.float64)
        adjacencies = {i: [] for i in range(n + 1)}
        edges: list = []

        for _, row in instance.iterrows():
            u, v, dist = int(row.u), int(row.v), float(row.duv)
            distance_matrix[u, v] = distance_matrix[v, u] = dist
            adjacencies[u].append((v, dist))
            adjacencies[v].append((u, dist))
            edges.append((u, v, dist))

        return cls(n, distance_matrix, adjacencies, edges)

    def get_distance(self, u: int, v: int) -> float:
        return self.distance_matrix[u, v]

    def __str__(self) -> str:
        return f"Graph(n={self.n}, edges={len(self.edges)})"
