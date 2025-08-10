import unittest
from itertools import groupby

def deduplicate(seq: list):

    seq_sorted = sorted(seq)
    unique = [k for k, _ in groupby(seq_sorted)]
    return unique


class TestCase(unittest.TestCase):
    def test(self):
        seq = [1, 1, 2, 3, 2, 4, 5, 4, 6]
        result = [1, 2, 3, 4, 5, 6]
        deduplicate1 = deduplicate(seq=seq)
        print(deduplicate1)
        self.assertEqual(deduplicate1, result)