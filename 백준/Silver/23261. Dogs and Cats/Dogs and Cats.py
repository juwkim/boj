g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    N, D, C, M = g()
    S = input()
    ans = 'YES'
    for i in range(N):
        if S[i] == 'C':
            if C:
                C -= 1
            else:
                if 'D' in S[i+1:]:
                    ans = 'NO'
                break
        else:
            if D:
                D -= 1
                C += M
            else:
                ans = 'NO'
                break
    print(f'Case #{_}:', ans)