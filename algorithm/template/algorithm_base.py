# algorithm_base.py
"""
Python 알고리즘 문제 풀이용 기본 패키지 세팅
"""

# ===== 표준 라이브러리 =====
import sys
import math
import heapq
import bisect
import itertools
import collections
import functools
import random
import statistics

# ===== 입출력 속도 최적화 =====
input = sys.stdin.readline  # 빠른 입력

# ===== 자료구조 단축 이름 =====
deque = collections.deque
Counter = collections.Counter
defaultdict = collections.defaultdict

# ===== 자주 쓰는 단축 함수 =====
def read_int():
    return int(input().strip())

def read_ints():
    return map(int, input().strip().split())

def read_list():
    return list(map(int, input().strip().split()))

# ===== 예시 사용 =====
if __name__ == "__main__":
    # 빠른 입력 예시
    n = read_int()
    arr = read_list()
    print("입력:", n, arr)

    # 조합 예시
    print("조합(2개씩):", list(itertools.combinations(arr, 2)))

    # 힙 예시
    heap = []
    for x in arr:
        heapq.heappush(heap, x)
    print("힙 pop:", heapq.heappop(heap))