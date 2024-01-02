import sys


def test_solve(s: str):
    return solve_is_palindrome(s)


def is_palindrome(s: str) -> bool:
    s_index = 0
    l_index = len(s) - 1
    while s_index < l_index and l_index > 0:
        while not str.isalnum(s[s_index]):
            s_index += 1
            if s_index >= len(s):
                return True
        while not str.isalnum(s[l_index]):
            l_index -= 1
            if l_index < 0:
                return True
        if s_index >= l_index:
            return True
        if str.lower(s[s_index]) != str.lower(s[l_index]):
            return False
        s_index += 1
        l_index -= 1
    return True


def solve_is_palindrome(s: str) -> bool:
    targets = []
    for char in s:
        if str.isalpha(char):
            targets.append(str.lower(char))

    while len(targets) > 1:
        if targets.pop(0) != targets.pop():
            return False
    return True


if __name__ == '__main__':
    t = str(sys.stdin.readline())

    m = solve_is_palindrome(t)
    print(m)
    # 점화식 (n + i) = (n) + k
