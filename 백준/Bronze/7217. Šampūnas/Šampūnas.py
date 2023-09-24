import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
check = bytearray(N + 1)
for _ in range(K):
    check[int(input())] = True

for i in range(1, N + 1):
    if check[i - 1] == False:
        check[i] = True
print(sum(check))