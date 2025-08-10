import unittest
from typing import Iterable, TypeVar, List

T = TypeVar("T")

def chunk(it: Iterable[T], size: int) -> List[List[T]]:
    buf: List[T] = []
    out: List[List[T]] = []
    for item in it:
        buf.append(item)
        if len(buf) == size:
            out.append(buf)
            buf = []
    if buf:
        out.append(buf)
    return out

print()  # [[0,1,2],[3,4,5],[6,7,8],[9]]

class TestSolution(unittest.TestCase):
    def test_chunk3(self):
        input_case = range(10)
        result = chunk(range(10), 3)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
