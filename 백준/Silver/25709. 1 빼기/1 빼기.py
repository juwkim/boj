import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cnt = 0
while True:
    s = str(N)
    cnt += 1
    idx = s.find('1')
    if idx == -1:
        N -= 1
    else:
        t = (s[:idx] + s[idx + 1:]).lstrip('0')
        if t == '':
            break
        N = int(t)
print(cnt)