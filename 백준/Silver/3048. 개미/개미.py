N1, N2 = map(int, input().split())
A, B = input(), input()
T = int(input())
buf = ['' for _ in range(N1 + N2)]
for i in range(N2):
    idx = i + max(0, N1 - max(0, T - i))
    buf[idx] = B[i]
idx = -1
for c in A:
    while buf[idx]:
        idx -= 1
    buf[idx] = c
print(*buf, sep='')