from unittest import TestCase
from simple_bags import solve_simple_bags


class Test(TestCase):

    def test_solve(self):
        n, k = 4, 7
        bags = [(6, 13),
                (4, 8),
                (3, 6),
                (5, 12)]
        value = solve_simple_bags(n, k, bags)
        self.assertEqual(value, 14)
