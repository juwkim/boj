def g(): return [*map(int, input().split())]

N = int(input())
A, B = sorted(g()), sorted(g())

score = 0
idx = 0
for num in A:
    while idx < N and B[idx] <= num:
        idx += 1
    if idx < N:
        score += 1
        idx += 1
    else:
        break
if score >= N // 2 + 1:
    print('YES')
else:
    print('NO')