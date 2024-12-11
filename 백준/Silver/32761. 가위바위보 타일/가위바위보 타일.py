N,S=open(0)
cnt = [0, 0, 0]
for c in S:
    for i in range(3):
        cnt[i] += "SPR"[(i + cnt[i]) % 3] == c
print(int(N)-max(cnt)//3*3)