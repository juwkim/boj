import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = [0, 0]
    input()
    for A in map(int, input().split()):
        cnt[A & 1] += 1
    a, b = sorted(cnt)
    print(("heeda0528", "amsminn")[b&1 and b > a])