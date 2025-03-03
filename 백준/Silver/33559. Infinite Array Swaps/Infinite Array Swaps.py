from collections import Counter
g = lambda: Counter(map(int, input().split()))

N = int(input())
A, B = g(), g()
cnt, Ai = 0, []
for k in A:
    num = min(A[k], B[k])
    A[k] -= num
    B[k] -= num
    cnt += num
    Ai += [k] * num
Bi = Ai[:]
for k, v in A.items(): Ai.extend([k] * v)
for k, v in B.items(): Bi.extend([k] * v)
print(cnt)
print(*Ai)
print(*Bi)