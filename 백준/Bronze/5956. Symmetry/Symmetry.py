N, M = map(int, input().split())
i = 0
while N%2 and M%2:
    i, N, M = i+1, N//2, M//2
print((4**i-1)//3)