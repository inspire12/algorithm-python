import sys
from unittest import TestCase


def solve_simple_bags(n, k, bags):
    knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    bags.append((0, 0))
    bags.sort(key=lambda a: a[0])
    m = 0
    for i in range(n + 1):
        for upper_weight in range(i, k + 1):
            weight = bags[i][0]
            value = bags[i][1]
            if upper_weight < weight:
                knapsack[i][upper_weight] = knapsack[i - 1][upper_weight]
            else:
                knapsack[i][upper_weight] = max(value + knapsack[i - 1][upper_weight - weight], knapsack[i - 1][upper_weight])
                m = max(m, knapsack[i][upper_weight])
    return m


if __name__ == '__main__':

    l = []
    n, k = map(int, sys.stdin.readline().split())
    for _ in range(0, n):
        a, b = map(int, sys.stdin.readline().split())
        l.append((a, b))

    m = solve_simple_bags(n, k, l)
    print(m)
    # 점화식 (n + i) = (n) + k


class Test(TestCase):

    def test_solve(self):
        n, k = 4, 7
        bags = [(6, 13),
                (4, 8),
                (3, 6),
                (5, 12)]
        value = solve_simple_bags(n, k, bags)
        self.assertEqual(value, 14)
