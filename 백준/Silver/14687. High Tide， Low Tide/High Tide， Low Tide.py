g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted(g())

low = nums[(N-1)//2::-1]
high = nums[(N+1)//2:]

for i in range(len(high)):
    print(low[i], high[i], end=' ')
if N & 1:
    print(low[-1])