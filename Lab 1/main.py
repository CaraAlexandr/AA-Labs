import math
import time
from decimal import Decimal
from prettytable import PrettyTable

import matplotlib.pyplot as plt


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


def fib_memoized(n):
    memo = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]


def fib_matrix(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = [[1, 1], [1, 0]]
        for i in range(2, n + 1):
            matrix = [[matrix[0][0] + matrix[0][1], matrix[0][0]], [matrix[0][0], matrix[1][0]]]
        return matrix[0][0]


def fib_binet(n):
    sqrt_5 = math.sqrt(5)
    phi = (Decimal(1) + Decimal(sqrt_5)) / 2
    psi = (Decimal(1) - Decimal(sqrt_5)) / 2
    return int((phi ** Decimal(n) - psi ** Decimal(n)) / Decimal(sqrt_5))


# ========================================================================================================

def time_fib_recursive(n):
    start = time.time()
    fib_recursive(n)
    end = time.time()
    return (end - start) * 1000


def time_fib_iterative(n):
    start = time.time()
    fib_iterative(n)
    end = time.time()
    return (end - start) * 1000


def time_fib_memoized(n):
    start = time.time()
    fib_memoized(n)
    end = time.time()
    return (end - start) * 1000


def time_fib_matrix(n):
    start = time.time()
    fib_matrix(n)
    end = time.time()
    return (end - start) * 1000


def time_fib_binet(n):
    start = time.time()
    fib_binet(n)
    end = time.time()
    return (end - start) * 1000


# ========================================================================================================

if __name__ == "__main__":
    vals = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32]
    n = len(vals)

    plt.plot([time_fib_recursive(vals[i]) for i in range(0, n)])
    plt.plot([time_fib_iterative(vals[i]) for i in range(0, n)])
    plt.plot([time_fib_memoized(vals[i]) for i in range(0, n)])
    plt.plot([time_fib_matrix(vals[i]) for i in range(0, n)])
    plt.plot([time_fib_binet(vals[i]) for i in range(0, n)])

    table = PrettyTable()
    table.field_names = ["n", "fib_recursive", "fib_iterative", "fib_memoized", "fib_matrix", "fib_binet"]
    for i in range(0, n):
        table.add_row([vals[i], time_fib_recursive(vals[i]), time_fib_iterative(vals[i]), time_fib_memoized(vals[i]),
                       time_fib_matrix(vals[i]), time_fib_binet(vals[i])])
    print(table)

    plt.legend(['fib_recursive', 'fib_iterative', 'fib_memoized', 'fib_matrix', 'fib_binet'])
    plt.title('Fibonacci')
    plt.xlabel(vals[0:n])
    plt.ylabel('time in milliseconds')

    plt.show()
