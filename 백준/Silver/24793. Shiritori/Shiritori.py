N = int(input())
check = set()
s = input()
check.add(s)
prev = s[-1]
ans = 'Fair Game'
for i in range(1, N):
    s = input()
    if s in check or s[0] != prev:
        ans = f'Player {(i & 1) + 1} lost'
        break
    prev = s[-1]
    check.add(s)
print(ans)