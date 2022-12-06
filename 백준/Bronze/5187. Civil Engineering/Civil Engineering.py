import sys
input = sys.stdin.readline

for cnt in range(1, 1 + int(input())):
    m, n = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    ans = 0
    for _ in range(n):
        h, w, d, i = map(int, input().split())
        ans += h * w * d * a[i-1]
    print(f'Data Set {cnt}:\n{ans}')