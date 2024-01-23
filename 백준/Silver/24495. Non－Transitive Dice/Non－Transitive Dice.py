import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product
def solve(dice1, dice2):
    a, b = 0, 0
    for p, q in product(dice1, dice2):
        if p > q: a += 1
        elif p < q: b += 1
    return (a > b) - (a < b)

for _ in range(int(input())):
    nums = g()
    A, B = nums[:4], nums[4:]
    check = solve(A, B)
    if check == 0:
        print("no")
        continue
    if check == 1:
        res1, res2 = -1, 1
    else:
        res1, res2 = 1, -1
    ans = "no"
    for l in product(range(1, 11), repeat=4):
        if solve(A, l) == res1 and solve(B, l) == res2:
            ans = "yes"
            break
    print(ans)