'''
제목: 
출처: https://www.acmicpc.net/problem/17404
idea: 비용의 최솟값, dp[n][color] = min(dp[n-1][(color + 1) %3], dp[n-1][(color + 2) %3]) + house[color]
난이도: Easy
'''
import unittest

import sys
INF = int(1e9)

def solution(house):

    colors = [0, 1, 2]
    l = len(house)
    answer = INF
    for first_color in range(3):
        dp = [[INF]*3 for _ in range(l)]
        dp[0][first_color] = house[0][first_color]

        for n in range(1, l):
            for color in colors:
                dp[n][color] = min(dp[n-1][(color + 1) %3], dp[n-1][(color + 2) %3]) + house[n][color]

        for last_color in range(3):
            if last_color != first_color:
                answer = min(answer, dp[l-1][last_color])

    return answer

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
        expected = 110
        self.assertEqual(solution(input_template), expected)

    def test_example_2(self):
        input_template = [[1, 100, 100],
[100, 1, 100],
[100, 100, 1]]
        expected = 3
        self.assertEqual(solution(input_template), expected)

    def test_example_3(self):
        input_template = [[1, 100, 100],
                          [100, 100, 100],
                          [1, 100, 100]]
        expected = 201
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

    def test_example_5(self):
        input_template = [[71, 39, 44],
[32, 83, 55],
[51, 37, 63],
[89, 29, 100],
[83, 58, 11],
[65, 13, 15],
[47, 25, 29],
[60, 66, 19]]
        expected = 253
        self.assertEqual(solution(input_template), expected)
