import unittest

def solution(input_string):
    answer_set = set()
    a_set = set()
    for i, s in enumerate(input_string):
        if i >= 1:
            if (input_string[i-1] != s) & (s in a_set):
                answer_set.add(s)
            else:
                a_set.add(s)
        else:
            a_set.add(s)
    if len(answer_set) == 0:
        return 'N'
    sorted_list = sorted(list(answer_set))
    return "".join(sorted_list)


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        input = 'edeaaabbccd'
        answer = 'de'
        self.assertEqual(solution(input), answer)  # add assertion here
    def test_something_2(self):
        input = 'eeddee'
        answer = 'e'
        self.assertEqual(solution(input), answer)  # add assertion here
    def test_something_3(self):
        input = 'string'
        answer = 'N'
        self.assertEqual(solution(input), answer)  # add assertion here
    def test_something_4(self):
        input = 'zbzbz'
        answer = 'bz'
        self.assertEqual(solution(input), answer)  # add assertion here


if __name__ == '__main__':
    unittest.main()
