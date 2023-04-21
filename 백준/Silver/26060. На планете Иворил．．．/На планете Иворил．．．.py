input()
ans = 0
for s in input().split():
    cnt = [0, 0, 0]    
    for i, t in enumerate(s):
        if t not in 'aeiouy':
            cnt[2] += 1
        cnt[(i & 1) ^ (t in 'aeiouy')] += 1
    ans += min(cnt)
print(ans)