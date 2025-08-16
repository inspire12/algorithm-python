import sys


def main():
    n = int(sys.stdin.readline())
    switch_list = [0]
    switch_list.extend(list(map(int, sys.stdin.readline().split())))

    students = []
    students_count = int(sys.stdin.readline())
    for _ in range(students_count):
        students.append(list(map(int, sys.stdin.readline().split())))

    for student in students:
        if student[0] == 1:  # 남학생
            num = student[1]
            for k in range(num, n + 1, num):
                switch_list[k] = change_switch(switch_list[k])
        else:  # 여학생
            idx = student[1]
            left_idx = right_idx = idx
            while left_idx >= 1 and right_idx <= n and switch_list[left_idx] == switch_list[right_idx]:

                switch_list[left_idx] = change_switch(switch_list[left_idx])
                if left_idx != right_idx:
                    switch_list[right_idx] = change_switch(switch_list[right_idx])
                left_idx = left_idx - 1
                right_idx = right_idx + 1

    for i in range(1, n + 1, 20):
        print(" ".join(map(str, switch_list[i:i + 20])))

def change_switch(i):
    return (i + 1) % 2


if __name__ == '__main__':
    main()

import unittest

from solve.baekjoon.testutil_boj import dedent_trim

import io


class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''8
0 1 0 1 0 0 0 1
2
1 3
2 3
''')
        expected_output = dedent_trim('''1 0 0 0 1 1 0 1''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
    def test_2(self):
        test_input = dedent_trim('''8
0 1 0 1 0 0 0 1
2
1 3
2 8''')
        expected_output = dedent_trim('''0 1 1 1 0 1 0 0''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
