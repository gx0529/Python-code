
�˻ʺ�����

from pip._vendor.msgpack.fallback import xrange

BOARD_SIZE = 8

def under_attack(col,queens):
    left = right = col
    for r,c in reversed(queens):
        left,right = left - 1,right + 1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0:
        return [[]]

    smaller_solution = solve(n-1)

    return [solution+[(n,i+1)]
        for i in xrange(BOARD_SIZE)
            for solution in smaller_solution
                if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE):
    print(answer)
