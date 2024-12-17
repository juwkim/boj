import sys
input = sys.stdin.readline

while (l:=[*map(int, input().split())])[1]:
    t, n, *x = l
    ans, s = [], set()
    def solve(i, num, nums):
        if i == n:
            return
        if num + x[i] < t:
            solve(i + 1, num + x[i], nums + [x[i]])
        elif num + x[i] == t:
            p = '+'.join(map(str, nums + [x[i]]))
            if p not in s:
                s.add(p)
                ans.append(p)
        solve(i + 1, num, nums)
    solve(0, 0, [])
    print(f'Sums of {t}:')
    if ans:
        for a in ans: print(a)
    else:
        print('NONE')