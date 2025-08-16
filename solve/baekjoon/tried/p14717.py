import io
import unittest
import sys

def main():
    #  1~ 10 10 개, 내가 뽑은 케이스 제외 18C2 18* 17 /2 개 케이스
    # 땡인 경우 11개, 땡이 아닌 경우 44개
    # 한 케이스 제외

    cards = []
    for c in range(1, 11):
        cards.extend([c, c])

    A, B = map(int, sys.stdin.readline().split())
    cards.remove(A)
    cards.remove(B)
    all_case = 153

    score_case = [0 for _ in range(10)]

    for i, a in enumerate(cards):
        for b in cards[i:]:
            if a == b:
                continue
            score_case[(a + b) %10] += 1


    if A == B:
        result = (A + (all_case-10)) / all_case
    #    땡인 경우
    else:
        score = (A + B) % 10
        win_case = sum(score_case[:score])
        result = win_case / all_case

    print(f"{result:.3f}")


if __name__ == '__main__':
    main()

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        test_input = "1 1"
        expected_output = "0.941\n"
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_example_2(self):
        test_input = "1 2"
        expected_output = "0.275\n"
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_example_3(self):
        test_input = "1 9"
        expected_output = "0.000\n"
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
