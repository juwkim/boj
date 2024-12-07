N = int(input())
S = input()
ans = [*S]
def solve(i, cnt):
    if i == N:
        if cnt == 0:
            print(''.join(ans))
            exit()
        return
    if ans[i] == 'G':
        if cnt > 0:
            ans[i] = ')'
            solve(i + 1, cnt - 1)
            ans[i] = 'G'
        ans[i] = '('
        solve(i + 1, cnt + 1)
        ans[i] = 'G'
    elif ans[i] == '(':
        solve(i + 1, cnt + 1)
    elif cnt:
        solve(i + 1, cnt - 1)
    else:
        return
solve(0, 0)