def solve():
    N = int(input())
    if N <= 9:
        return 1
    for A in range(2, 10):
        for B in range(1, 10):
            if N == A * B:
                return 1
    return 0
print(solve())