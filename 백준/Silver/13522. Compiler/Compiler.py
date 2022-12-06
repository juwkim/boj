def solve(N):
    if N == 0:
        return ['ZE A']
    if N == 1:
        return ['ST A']
    if N == 2:
        return ['PH X', 'PH X', 'AD', 'PL A']
    cnt, res = min([(cnt, solve(N//cnt)) for cnt in range(2, 4)], key=lambda x: len(x[1]) + 2 * (x[0] + N % x[0]))
    res.extend(['PH A']*cnt)
    res.extend(['AD']*(cnt-1))
    res.extend(['PH X', 'AD']*(N%cnt))
    res.append('PL A')
    return res
ans = solve(int(input()))
print('ST X', *ans, 'DI A', sep='\n')