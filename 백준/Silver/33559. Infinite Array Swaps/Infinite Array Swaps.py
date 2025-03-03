from collections import Counter
g = lambda: Counter(map(int, input().split()))

N = int(input())
A, B = g(), g()
cnt, l = 0, []
for k in A:
    num = min(A[k], B[k])
    A[k] -= num
    B[k] -= num
    cnt += num
    l += [k] * num
print(cnt)
Ai = l[:]
for k, v in A.items():
    Ai.extend([k] * v)
print(*Ai)
Bi = l[:]
for k, v in B.items():
    Bi.extend([k] * v)
print(*Bi)