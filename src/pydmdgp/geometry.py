import numpy as np
from pydmdgp.exceptions import NoIntersectionError

import numpy as np


def intersect_3_spheres(a: np.ndarray, ra: float, b: np.ndarray, rb: float,
                        c: np.ndarray,
                        rc: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Calcula a interseção de três esferas com centros a, b, c e raios ra, rb, rc.
    Retorna uma tupla com os dois pontos de interseção (vetores NumPy).
    """

    u = b - a
    v = c - a
    n = np.cross(u, v)
    n_norm = np.linalg.norm(n)
    if n_norm < 1e-9:
        raise NoIntersectionError("Os centros são colineares.")
    n = n / n_norm

    M = np.vstack([u, v, n])

    w = 0.5 * np.array([
        np.dot(b, b) - np.dot(a, a) + ra**2 - rb**2,
        np.dot(c, c) - np.dot(a, a) + ra**2 - rc**2, 2 * np.dot(n, a)
    ])

    try:
        p = np.linalg.solve(M, w)
    except np.linalg.LinAlgError:
        raise NoIntersectionError(
            "Matriz singular —  possivelmente centros colineares.")

    d_sq = float(ra**2 - np.linalg.norm(p - a)**2)
    if d_sq < -1e-9:
        raise NoIntersectionError("As esferas não se intersectam.")

    dp = np.sqrt(max(0.0, d_sq))

    p1 = p + dp * n
    p2 = p - dp * n

    return p1, p2


# def _cosine_angle(p1: np.ndarray, p2: np.ndarray, p3: np.ndarray) -> float:
#     """Calcula o cosseno do ângulo no ponto p1 formado pelo triângulo p1-p2-p3."""
#     vec1 = p2 - p1
#     vec2 = p3 - p1
#     return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# def intersect_3_spheres(c1: np.ndarray, r1: float, c2: np.ndarray, r2: float,
#                         c3: np.ndarray,
#                         r3: float) -> tuple[np.ndarray, np.ndarray]:
#     """
#     Calcula a interseção de 3 esferas.
#     Centros c1, c2, c3 são vetores NumPy de 3 elementos.
#     Retorna uma tupla com os dois pontos de interseção (vetores NumPy).
#     """

#     sphere_data = [
#         (_cosine_angle(c1, c2, c3), (c1, r1, c2, r2, c3, r3)),
#         (_cosine_angle(c2, c1, c3), (c2, r2, c1, r1, c3, r3)),
#         (_cosine_angle(c3, c1, c2), (c3, r3, c1, r1, c2, r2)),
#     ]
#     _, (u, du, v, dv, w, dw) = min(sphere_data, key=lambda item: item[0])

#     print(f"Interseção de esferas: {u}, {v}, {w} com raios {du}, {dv}, {dw}")

#     n = np.cross(v - u, w - u)
#     n = n / np.linalg.norm(n)

#     A = np.array([v - u, w - u, n]).T

#     b = 0.5 * np.array([(v @ v - dv**2) - (u @ u - du**2),
#                         (w @ w - dw**2) - (u @ u - du**2), 2 * (u @ n)])

#     p = np.linalg.solve(A, b)

#     dpu = np.linalg.norm(p - u)

#     val_sqrt = du**2 - dpu**2
#     if val_sqrt < -1e-9:
#         raise NoIntersectionError("As esferas não se interceptam.")

#     dp = np.sqrt(max(0.0, float(val_sqrt)))

#     p1 = p + dp * n
#     p2 = p - dp * n

#     return p1, p2

if __name__ == "__main__":
    # Teste de interseção de esferas
    a = np.array([0.0, 0.0, 0.0])
    b = np.array([1.0, 0.0, 0.0])
    c = np.array([0.5, 1.0, 0.0])
    ra = 1.0
    rb = 1.0
    rc = 1.0

    try:
        p1, p2 = intersect_3_spheres(a, ra, b, rb, c, rc)
        print("Ponto de interseção 1:", p1)
        print("Ponto de interseção 2:", p2)
    except NoIntersectionError as e:
        print("Erro:", e)
