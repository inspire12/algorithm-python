import sys
def main():
    l = sys.stdin.readline().strip()



if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''4 5 1
1 2
1 3
1 4
2 4
3 4
''')
        expected_output = dedent_trim('''1 2 4 3
1 2 3 4
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
