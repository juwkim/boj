N = int(input())
if N <= 2:
    print(4)
else:
    print(N + (N & 1))