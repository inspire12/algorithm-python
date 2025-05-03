import sys
from unittest import TestCase

'''
    제목:
    출처:
    idea:
    난이도: 
'''
def solve_coin(n: int, coins: list, goal_money: int):
    optimal_values = [0 for _ in range(goal_money + 1)]

    optimal_values[0] = 1
    for coin_index, coin in enumerate(coins):
        for money_index in range(coin, goal_money + 1):
            if money_index - coin >= 0:
                # 다른 동전으로 이 계산을 맞출 수 있는 경우의 수가 있는지
                optimal_values[money_index] = optimal_values[money_index] + optimal_values[money_index - coin]

    return optimal_values[goal_money]


def solve_coin_2(n: int, coins: list, goal_money: int):
    optimal_values = [0 for _ in range(goal_money + 1)]
    pass


if __name__ == '__main__':

    l = []
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline().split())
        coins = map(int, sys.stdin.readline().split())
        money = int(sys.stdin.readline())

        m = solve_coin(n, coins, money)
        print(m)
    # 점화식 (n + i) = (n) + k



class Test(TestCase):

    def test_solve_case_1(self):
        n = 2
        coins = [1, 2]
        money = 1000
        value = solve_coin(n, coins, money)
        self.assertEqual(501, value)

    def test_solve_case_2(self):
        n = 3
        coins = [1, 5, 10]
        money = 100
        value = solve_coin(n, coins, money)
        self.assertEqual(121, value)

    def test_solve_case_3(self):
        n = 2
        coins = [5, 7]
        money = 22
        value = solve_coin(n, coins, money)
        self.assertEqual(1, value)


    def test_solve_2_case_1(self):
        n = 2
        coins = [1, 2]
        money = 1000
        value = solve_coin_2(n, coins, money)
        self.assertEqual(501, value)

    def test_solve_2_case_2(self):
        n = 3
        coins = [1, 5, 10]
        money = 100
        value = solve_coin_2(n, coins, money)
        self.assertEqual(121, value)

    def test_solve_2_case_3(self):
        n = 2
        coins = [5, 7]
        money = 22
        value = solve_coin_2(n, coins, money)
        self.assertEqual(1, value)