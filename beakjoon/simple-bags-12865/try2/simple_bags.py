import sys

N = 4
K = 7

things = [6, 13,
          4, 8,
          3, 6,
          5, 12]


def solve_simple_bags(n, k, bags):
    sorted(wv, key=lambda a: a[0])
    print(wv)
    knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    bags.append((0, 0))
    bags.sort(key=lambda a: a[0])
    for i in range(n):

    return n


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())

    wv = []

    for _ in range(n):
        weight, value = map(int, sys.stdin.readline().split())
        wv.append((weight, value))

    print(solve_simple_bags(n, k, wv))

