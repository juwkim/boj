g = lambda: [*map(int, input().split())]

N = int(input())
A = g()
l = max(A) + 1
buf = [0] * l
for num in A:
    for i in range(num+1, l):
        buf[i] += 1
for num in A:
    print(buf[num], end=' ')
    buf[num] += 1