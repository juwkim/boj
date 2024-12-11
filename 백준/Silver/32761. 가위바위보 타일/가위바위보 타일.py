N = int(input())
cnt = [0, 0, 0]
for c in input():
    for i in range(3):
        cnt[i] += "SPR"[(i + cnt[i]) % 3] == c
print(N - max(cnt)//3*3)