import sys
from collections import Counter
from unittest import TestCase

'''
    제목:
    출처:
    idea:
    난이도: 
'''
def solve_dice_world(a, b, c):
    dice = Counter([a, b, c])
    if len(dice) == 1:
        return 10_000 + a * 1_000
    if len(dice) == 2:
        k = dice.most_common(1)[0][0]
        return 1_000 + k * 100
    max_value = max(a, b, c)
    return max_value * 100

if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())
    m = solve_dice_world(a, b, c)
    print(m)


class Test(TestCase):
    def test_case1(self):
        value = solve_dice_world(3, 3, 6)
        self.assertEqual(value, 1300)

    def test_case2(self):
        value = solve_dice_world(2, 2, 2)
        self.assertEqual(value, 12000)

    def test_case2(self):
        value = solve_dice_world(6, 2, 5)
        self.assertEqual(value, 600)