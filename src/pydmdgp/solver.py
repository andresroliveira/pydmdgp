import numpy as np
from .graph import Graph
from .geometry import intersect_3_spheres
from .exceptions import NoIntersectionError, NoSolutionError


def _initialize_coordinates(graph: Graph) -> np.ndarray:
    """
    Posiciona os 3 primeiros átomos para definir um sistema de coordenadas.
    """
    X = np.zeros((graph.n + 1, 3))

    d12 = graph.get_distance(1, 2)
    d13 = graph.get_distance(1, 3)
    d23 = graph.get_distance(2, 3)

    if not all([d12 > 0, d13 > 0, d23 > 0]):
        raise ValueError(
            "As distâncias entre os 3 primeiros átomos devem ser maiores que zero."
        )

    x1 = np.array([0.0, 0.0, 0.0])
    x2 = np.array([-d12, 0.0, 0.0])
    cos_theta = (d12**2 + d23**2 - d13**2) / (2 * d12 * d23)
    sin_theta = np.sqrt(1 - cos_theta**2)

    # x3 no plano xy
    x3 = np.array([-d12 + d23 * cos_theta, d23 * sin_theta, 0.0])

    X[1] = x1
    X[2] = x2
    X[3] = x3

    return X


def _calculate_loss(graph: Graph, X: np.ndarray, k: int) -> float:
    """
    Calcula o erro para um átomo 'k' recém-posicionado.
    O erro é a média dos quadrados das diferenças das distâncias.
    """

    return float(
        np.mean([(np.linalg.norm(X[u] - X[k])**2 - duk**2)**2
                 for u, duk in graph.adjacencies[k] if u < k]))


def _next_point(graph: Graph, X: np.ndarray, k: int, b: int) -> np.ndarray:
    d1 = graph.get_distance(k, k - 3)
    d2 = graph.get_distance(k, k - 2)
    d3 = graph.get_distance(k, k - 1)

    x1 = X[k - 3]
    x2 = X[k - 2]
    x3 = X[k - 1]

    pp = intersect_3_spheres(x1, d1, x2, d2, x3, d3)

    return pp[b]


def solve(graph: Graph, delta: float = 1e-4) -> np.ndarray:
    """
    Resolve o DMDGP para um grafo com ordem de discretização pré-definida.

    Esta função assume que a ordem dos vértices (1, 2, ..., n) é uma ordem de
    discretização válida, onde cada átomo 'k' >= 4 tem distâncias conhecidas
    para os átomos k-1, k-2 e k-3.

    Args:
        graph: Uma instância da classe Graph.
        delta: A tolerância de erro para a poda (pruning).

    Returns:
        Uma matriz NumPy de formato (n+1, 3) com as coordenadas 3D dos átomos.

    Raises:
        NoSolutionError: Se nenhuma solução válida for encontrada.
    """
    n = graph.n
    if n < 3:
        raise ValueError("O grafo precisa de pelo menos 3 átomos.")

    X = _initialize_coordinates(graph)

    branch = np.zeros(n + 1, dtype=int)
    visited = np.zeros(n + 1, dtype=int)
    visited[1:4] = 1

    k = 4

    while k > 3:
        visited[k] += 1
        X[k] = _next_point(graph, X, k, branch[k])
        err = _calculate_loss(graph, X, k)

        prune = err > delta

        if prune:
            if branch[k] == 0:
                branch[k] = 1
                # Resetar os próximos ramos
                for i in range(k + 1, n + 1):
                    branch[i] = 0
                k -= 1
            else:
                branch[k] = 0
                k -= 1
        else:
            if k == n:
                return X
            else:
                k += 1

    print("Unreachable code reached. This should not happen.")
    raise NoSolutionError("Nenhuma solução válida encontrada para o DMDGP.")
