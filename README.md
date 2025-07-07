# pydmdgp

Resolução do problema de realização molecular (DMDGP) em Python.

## Descrição

Este projeto implementa um solver para o Discretizable Molecular Distance Geometry Problem (DMDGP), utilizando técnicas de branch-and-prune para reconstrução de estruturas moleculares a partir de distâncias.

## Estrutura

- `src/pydmdgp/` — Código-fonte principal (solver, geometria, grafo, exceções)
- `data/` — Instâncias de entrada em formato CSV
- `tests/` — Testes automatizados
- `run_solver.py` — Script para executar o solver em uma instância

## Como usar

```bash
git clone https://github.com/andresroliveira/pydmdgp/
cd pydmdgp
# python -m venv venv && source venv/bin/activate  # (opcional, para criar um ambiente virtual, mas recomendado)
pip install -e .
```

## Executando o Solver

```bash
python run_solver.py
```

## Executando Testes

```bash
pytest tests/
```
