import sys
def main():
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    left = 0
    right = len(s) - 1
    count = 0
    while left < right:
        if s[left] != s[right]:
            count+= 1
        left += 1
        right -= 1
    print(count)


if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_0(self):
        test_input = dedent_trim('''7
stsssss
    ''')
        expected_output = dedent_trim('''1
    ''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
    def test_1(self):
        test_input = dedent_trim('''7
ststtss
''')
        expected_output = dedent_trim('''2
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''8
ttsststt
''')
        expected_output = dedent_trim('''1
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_3(self):
        test_input = dedent_trim('''6
ssttss
''')
        expected_output = dedent_trim('''0''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
