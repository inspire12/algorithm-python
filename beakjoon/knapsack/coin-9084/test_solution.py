from unittest import TestCase
from coin import solve_coin, solve_coin_2


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