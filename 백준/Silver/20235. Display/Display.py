import sys
input = lambda: sys.stdin.readline().rstrip()

n, w, h, s = map(int, input().split())
max_cnt = 0
for _ in range(n):
    c = input()
    cnt = 2 * max(('.' + input()).count(".#") for _ in range(h))
    if cnt > max_cnt:
        max_cnt = cnt
        alpha = c
print(alpha * ((s + max_cnt - 1) // max_cnt))