"""
pydmdgp: Um solver em Python para o Problema de Geometria de Distâncias Moleculares Discretizável (DMDGP).

Este pacote fornece ferramentas para criar, analisar e resolver instâncias do DMDGP
usando um algoritmo de Branch-and-Prune.
"""

# É uma excelente prática definir a versão do seu pacote aqui.
__version__ = "0.1.0"

from .exceptions import (DMDGPError, NoSolutionError, NoIntersectionError,
                         DiscretizationError)
from .graph import Graph
from .solver import solve

# __all__ é uma lista que define explicitamente quais nomes serão importados
# quando um usuário fizer `from pydmdgp import *`.
__all__ = [
    # exceptions.py
    "DMDGPError",
    "NoSolutionError",
    "NoIntersectionError",
    "DiscretizationError",

    # graph.py
    "Graph",

    # solver.py
    "solve",
]
