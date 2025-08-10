import pandas as pd
import unittest

def deduplicate():
    df = pd.read_csv("users.csv")
    df = (
        df.drop_duplicates(subset=["email"], keep="first")  # 이메일 중복 제거
        .reset_index(drop=True)
    )
    return df


class TestSolution(unittest.TestCase):
    def test(self):
        deduplicate1 = deduplicate()
        print(deduplicate1)