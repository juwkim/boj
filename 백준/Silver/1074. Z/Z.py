def solve(N, r, c):
    if N == 0:
        return 0
    else:
        div = 2**(N-1)
        count = ((r >= div) * 2 + (c >= div)) * div**2
        return count + solve(N-1, r % div, c % div)

print(solve(*map(int, input().split())))