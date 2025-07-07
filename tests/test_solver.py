# tests/test_solver.py
import pytest
from pydmdgp import Graph, solve, NoSolutionError


def test_graph_loading():
    """Testa se o grafo é carregado corretamente do arquivo de dados."""
    graph = Graph.from_csv("data/instance.csv")
    assert graph.n > 0
    assert graph.get_distance(1, 2) > 0


def test_solver_smoke_test():
    """
    Um "teste de fumaça": verifica se o solver roda sem quebrar e retorna
    o formato de dados esperado para a instância de teste.
    """
    graph = Graph.from_csv("data/instance.csv")
    try:
        coordinates = solve(graph)
        # Verifica se o formato da saída está correto (n+1, 3)
        assert coordinates.shape == (graph.n + 1, 3)
    except NoSolutionError:
        # É aceitável que o solver não encontre uma solução,
        # mas ele não deve quebrar com um erro inesperado.
        pytest.skip(
            "Solver não encontrou solução para a instância de teste, pulando o teste."
        )
