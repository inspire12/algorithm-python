'''
제목: 
출처: https://www.acmicpc.net/problem/1149
idea: 비용의 최솟값, dp[n][color] = min(dp[n-1][(color + 1) %3], dp[n-1][(color + 2) %3]) + house[n][color]
난이도: Easy
'''
import unittest

import sys

def solution(house):

    colors = [0, 1, 2]
    l = len(house)
    dp = [[0] * len(colors) for _ in range(l)]
    for n in range(l):
        if n == 0:
            dp[0][0] = int(house[0][0])
            dp[0][1] = int(house[0][1])
            dp[0][2] = int(house[0][2])
        else:
            for color in colors:
                dp[n][color] = min(dp[n-1][(color + 1) %3], dp[n-1][(color + 2) %3]) + house[n][color]

    return min(dp[l-1][0], dp[l-1][1], dp[l-1][2])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    house_cost = [[0] * 3 for _ in range(n)]
    for i in range(n):
        house_cost[i][0], house_cost[i][1], house_cost[i][2] = map(int, sys.stdin.readline().split())

    r = solution(house_cost)
    print(r)

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        input_template = [[26, 40, 83]
,[49 ,60 ,57]
,[13 ,89 ,99]]
        expected = 96
        self.assertEqual(solution(input_template), expected)

    def test_example_4(self):
        input_template = [[30, 19, 5],
[64, 77, 64],
[15, 19, 97],
[4 ,71 ,57],
[90, 86, 84],
[93, 32, 91]]
        expected = 208
        self.assertEqual(solution(input_template), expected)

