N = int(input())
ans = 1e18
def solve(s):
    global ans
    num = int(s)
    d1, d2 = abs(num - N), abs(ans - N)
    if d1 < d2 or (d1 == d2 and num < ans):
        ans = num
    if len(s) == 10:
        return
    for i in "0123456789":
        if i not in s:
            solve(s + i)
for i in "123456789":
    solve(i)
print(ans)