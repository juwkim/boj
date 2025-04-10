import sys
input = sys.stdin.readline

for _ in range(100):
    cnt = sum(0.25 < float(input()) < 0.75 for _ in range(5000))
    print('AB'[cnt > 3000])