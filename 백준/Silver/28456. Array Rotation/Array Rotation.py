g = lambda: [*map(int, input().split())]

N = int(input())
A = [g() for _ in range(N)]
for _ in range(int(input())):
    s = input()
    if s[0] == '1':
        i = int(s.split()[1]) - 1
        A[i] = [A[i][-1]] + A[i][:-1]
    else:
        A = [list(reversed(l)) for l in zip(*A)]
for l in A:
    print(*l)