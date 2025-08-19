import sys



def dfs(node, depth):
    for key in sorted(node.keys()):
        print("--" * depth + key)
        dfs(node[key], depth + 1)

def main():
    N = int(input().strip())
    trie = {}
    for _ in range(N):
        parts = input().split()
        K, foods = int(parts[0]), parts[1:]
        node = trie
        for f in foods:
            if f not in node:
                node[f] = {}
            node = node[f]
    dfs(trie, 0)

if __name__ == '__main__':
    main()

import io
import unittest
from solve.baekjoon.testutil_boj import dedent_trim


class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''3
2 B A
4 A B C D
2 A C
''')
        expected_output = dedent_trim('''A
--B
----C
------D
--C
B
--A
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_2(self):
        test_input = dedent_trim('''4
2 KIWI BANANA
2 KIWI APPLE
2 APPLE APPLE
3 APPLE BANANA KIWI
''')
        expected_output = dedent_trim('''APPLE
--APPLE
--BANANA
----KIWI
KIWI
--APPLE
--BANANA
''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
