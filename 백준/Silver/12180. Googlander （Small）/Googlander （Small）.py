def solve(R, C):
    if C == 1: return 1
    return sum(solve(C - 1, i + 1) for i in range(R))

for i in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    print(f'Case #{i}: {solve(R, C)}')