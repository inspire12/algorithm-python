from unittest import TestCase
from dice_world import solve_dice_world


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
