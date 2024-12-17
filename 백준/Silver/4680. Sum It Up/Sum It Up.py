import sys
input = sys.stdin.readline

while (l:=[*map(int, input().split())])[1]:
    t, n, *x = l
    print(f'Sums of {t}:')
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
    if ans:
        for line in ans:
            print(line)
    else:
        print('NONE')