N = int(input())
for i in range(1, N):
    print((i * '*').rjust(N))
for i in range(N, 0, -1):
    print((i * '*').rjust(N))