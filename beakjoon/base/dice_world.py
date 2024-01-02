import sys
from collections import Counter


def solve_dice_world(a, b, c):
    dice = Counter([a, b, c])

    if len(dice) == 1:
        return 10_000 + a * 1_000
    if len(dice) == 2:
        k = dice.most_common(1)[0][0]
        return 1_000 + k * 100
    max_value = max(a, b, c)
    return max_value * 100


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())
    m = solve_dice_world(a, b, c)
    print(m)

