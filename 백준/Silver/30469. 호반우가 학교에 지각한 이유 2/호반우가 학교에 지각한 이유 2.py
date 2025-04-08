def solve():
    A, B, N = input().split()
    if B[0] in "24568":
        return -1
    N = int(N)
    if A[1] == '9':
        return A + '7' + '1' * (N - 5) + B
    return A + '1' * (N - 4) + B
print(solve())