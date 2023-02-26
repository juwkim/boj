input()
cur = 1
ans = 0
for c in input():
    if c == 'L':
        cur = max(cur - 1, 1)
    else:
        cur = min(cur + 1, 3)
    ans += cur == 3
print(ans)