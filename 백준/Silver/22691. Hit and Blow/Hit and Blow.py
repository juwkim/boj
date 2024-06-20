import sys
input = sys.stdin.readline
from itertools import permutations

def f(A, B):
    a, b = str(A).zfill(4), str(B).zfill(4)
    res = [0, 0]
    for i in range(4):
        for j in range(4):
            if a[i] == b[j]:
                res[i != j] += 1
    return res

nums = ["".join(map(str, i)) for i in permutations(range(10), 4)]
while n:=int(input()):
    v = [1] * 5040
    for _ in range(n):
        x, hit, blow = map(int, input().split())
        for j, s in enumerate(nums):
            v[j] &= f(s, x) == [hit, blow]
    l = [nums[i] for i in range(5040) if v[i]]
    if len(l) == 1:
        print(l[0])
        continue
    res = -1
    for num in nums:
        p = [[0] * 5 for _ in range(5)]
        for s in l:
            h, b = f(s, num)
            p[h][b] += 1
            if p[h][b] > 1:
                break
        if all(all(i <= 1 for i in j) for j in p):
            res = num
            break
    print("????" if res == -1 else res)