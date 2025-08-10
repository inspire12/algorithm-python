import unittest


def calc_time(diffs, times, level):
    t = times[0]
    for i in range(1, len(diffs)):
        if diffs[i] > level:
            t += (diffs[i]-level)*(times[i]+times[i-1])
        t += times[i]
        if t > limit:
            break
    return t


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
