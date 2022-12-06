g = lambda: [*map(int, input().split())]

check = [*range(1, 10)]
def solve():
    l = [g() for _ in range(9)]
    if any(check != sorted(l[i][j:j+3] + l[i+1][j:j+3] + l[i+2][j:j+3]) for i in range(0, 9, 3) for j in range(0, 9, 3)):
        return 'INCORRECT'
    l += [*zip(*l)]
    if any(check != sorted(line) for line in l):
        return 'INCORRECT'
    return 'CORRECT'

N = int(input())
for i in range(1, N):
    print(f'Case {i}:', solve())
    input()
if N:
    print(f'Case {N}:', solve())