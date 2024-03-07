N = int(input())
i = 1
while N > i:
    N -= i
    i <<= 1
print(N * 2 - 1)