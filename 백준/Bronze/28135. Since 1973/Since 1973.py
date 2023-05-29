N = input()
ans = 0
cur = 1
while True:
    ans += 1
    if N in str(cur):
        break
    if '50' in str(cur):
        ans += 1
    cur += 1
print(ans)