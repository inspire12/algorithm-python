import sys


def solve_simple_bags(n, k, bags):
    knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    bags.append((0, 0))
    bags.sort(key=lambda a: a[0])
    m = 0
    for i in range(n + 1):
        for j in range(i, k + 1):
            weight = bags[i][0]
            value = bags[i][1]
            if j < weight:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
                m = max(m, knapsack[i][j])
    print(m)


if __name__ == '__main__':

    l = []
    n, k = map(int, sys.stdin.readline().split())
    for _ in range(0, n):
        a, b = map(int, sys.stdin.readline().split())
        l.append((a, b))

    solve_simple_bags(n, k, l)
    # 점화식 (n + i) = (n) + k
