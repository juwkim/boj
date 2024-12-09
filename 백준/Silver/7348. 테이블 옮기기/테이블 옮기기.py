import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = [0] * 200
    for _ in range(int(input())):
        s, t = sorted(map(int, input().split()))
        for i in range((s - 1) // 2, (t + 1) // 2):
            cnt[i] += 1
    print(max(cnt) * 10)