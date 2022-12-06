import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

buf = []
for _ in range(int(input())):
    buf.append(min(g()))
buf.sort()
L = int(input())

total_len = 0
last_len = buf[0]
cnt = 1
for i in range(1, len(buf)):
    if L > total_len + (last_len + buf[i]) / 2:
        cnt += 1
        total_len += last_len
        last_len = buf[i]
print(cnt)