cnt = [0, 0, 0, 0]
N = int(input())
for num in map(int, input().split()):
    cnt[num] += 1
l = sorted([(i, j) for i in range(4) for j in range(4)], key=lambda x: x[0] ^ x[1], reverse=True)
ans = 0
for i, j in l:
    m = min(cnt[i], cnt[j])
    ans += m * (i ^ j)
    cnt[i] -= m
    cnt[j] -= m
print(ans)