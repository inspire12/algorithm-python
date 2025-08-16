# testutil_boj.py
import io
import sys
import textwrap
from contextlib import contextmanager, redirect_stdout

def dedent_trim(s: str) -> str:
    """테스트용 멀티라인 문자열의 들여쓰기를 정리하고
    앞/뒤 공백 라인을 제거합니다."""
    return textwrap.dedent(s).lstrip("\n").rstrip()

@contextmanager
def patch_stdin(input_text: str):
    """sys.stdin을 지정한 문자열로 임시 교체"""
    old_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(input_text)
        yield
    finally:
        sys.stdin = old_stdin

def run_io(main_func, input_text: str) -> str:
    """입력 문자열로 main_func를 실행하고 표준 출력을 문자열로 반환"""
    buf = io.StringIO()
    with patch_stdin(input_text), redirect_stdout(buf):
        main_func()
    return buf.getvalue()

def assertIO(testcase, main_func, input_text: str, expected_text: str, strict=True):
    """
    unittest.TestCase에서 한 줄로 입력/출력 비교.
    strict=False 이면 양끝 공백/개행 차이를 무시하고 비교합니다.
    """
    out = run_io(main_func, input_text)
    if strict:
        testcase.assertEqual(out, expected_text)
    else:
        testcase.assertEqual(out.strip(), expected_text.strip())


import io
import unittest
# from tried.baekjoon.testutil_boj import dedent_trim
class TestSolution(unittest.TestCase):
    def test_1(self):
        test_input = dedent_trim('''
            4 5 1
            1 2
            1 3
            1 4
            2 4
            3 4
        ''')
        expected_output = dedent_trim('''
            1 2 4 3
            1 2 3 4
        ''') + '\n'

        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        # main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
