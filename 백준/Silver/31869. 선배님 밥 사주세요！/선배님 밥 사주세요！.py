import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dic, day = {}, {}
for _ in range(N):
    name, w, d, p = input().split()
    dic[name] = int(p)
    day[name] = (int(w) - 1) * 7 + int(d)
check = bytearray(70)
for _ in range(N):
    name, p = input().split()
    if dic[name] <= int(p):
        check[day[name]] = 1
ans, cnt = 0, 0
for b in check:
    if b:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
if cnt:
    ans = max(ans, cnt)
print(ans)