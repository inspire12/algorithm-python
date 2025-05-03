from unittest import TestCase

'''
    제목:
    출처:
    idea:
    난이도: 
'''
def solve(a: list) -> int:
    return sum(a)


class TestSolution(TestCase):

    def test_something_1(self):
        l = [0, 1, 2, 3, 4]
        print(solve(l))
