*n, l = map(int, input().split())
n = sorted(zip(n[:3], n[3:]), reverse=True)
cnt = 0
for i in range(3):
    a = min(n[i][1], l // n[i][0] + (l % n[i][0] != 0))
    l -= n[i][0] * a
    cnt += a
    if l <= 0:
        break
print([cnt, 0][l > 0])