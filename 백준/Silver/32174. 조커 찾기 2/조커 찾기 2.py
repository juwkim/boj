import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

s = [0]
N, M = g()
for _ in range(M):
    cmd, num = g()
    match cmd:
        case 1:
            s.append((s[-1] + num) % N)
        case 2:
            s.append((s[-1] - num) % N)
        case 3:
            s.append(s[num])
print(s[M] + 1)