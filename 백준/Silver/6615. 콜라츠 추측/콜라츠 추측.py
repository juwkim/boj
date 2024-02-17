import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0:
        break
    p, q = A, B
    dic = {p: 0}
    step = 1
    while p != 1:
        if p & 1: p = 3 * p + 1
        else: p >>= 1
        dic[p] = step
        step += 1
    step = 0
    while q not in dic:
        if q & 1: q = 3 * q + 1
        else: q >>= 1
        step += 1
    ans = f"{A} needs {dic[q]} steps, {B} needs {step} steps, they meet at {q}"
    print(ans)