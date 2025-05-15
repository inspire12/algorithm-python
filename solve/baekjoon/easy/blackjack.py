'''
제목: blackjack
출처: https://www.acmicpc.net/problem/2798
idea: 최대한 가까운 카드 3장의 합
난이도: Easy
'''
import unittest
import sys

def solution(cards, m):
    cards = sorted(cards)
    t = len(cards)
    card = 0
    for i1 in range(t) :
        if cards[i1] > m:
            return card
        for i2 in range(i1 + 1, t):
            if cards[i1] + cards[i2] > m:
                return card
            for i3 in range(i2 + 1, t):
                tmp = cards[i1] + cards[i2] + cards[i3]
                if tmp <= m:
                    card = max(tmp, card)
    return card

if __name__ == '__main__':
    t, m = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    print(solution(cards, m))

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        t, m = 5, 21
        cards = [5, 6, 7, 8, 9]
        answer = 21
        self.assertEqual(solution(cards, m), answer)

    def test_example_2(self):
        t, m = 10, 500
        cards = list(map(int, '93 181 245 214 315 36 185 138 216 295'.split()))
        answer = 497
        self.assertEqual(solution(cards, m), answer)

