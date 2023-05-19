import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = A.shape[0]  # Assuming A is a square matrix
    L = np.eye(n)  # Initialize L as an identity matrix
    U = np.copy(A)  # Initialize U as a copy of A
    P = np.eye(n)  # Initialize P as an identity matrix

    for k in range(n - 1):
        if permute:
            # Partial pivoting
            pivot_index = np.argmax(np.abs(U[k:, k])) + k
            U[[k, pivot_index], k:] = U[[pivot_index, k], k:]
            L[[k, pivot_index], :k] = L[[pivot_index, k], :k]
            P[[k, pivot_index], :] = P[[pivot_index, k], :]

        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return L, U, P


def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    n = L.shape[0]  # Assuming L is a square matrix

    # Permute b according to P
    b_permuted = np.matmul(P, b)

    # Solve Ly = b_permuted using forward substitution with permutation
    y = np.zeros(n)
    for i in range(n):
        y[i] = b_permuted[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y using backward substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x



def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 14  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"
