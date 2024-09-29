input()
ans, cnt = 0, -100
for c in input():
    if c == 'A':
        ans += cnt == 1
        cnt = 0
    elif c == 'N':
        cnt += 1
print(ans)