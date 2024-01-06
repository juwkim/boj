import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
pos, neg, zero = [], [], False
ans = 0
for _ in range(N):
    num = int(input())
    if num == 1:
        ans += 1
        continue
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero = True
pos.sort(reverse=True)
neg.sort()

if len(pos) % 2 == 1:
    ans += pos[-1]
if len(neg) % 2 == 1 and not zero:
    ans += neg[-1]
ans += sum(pos[i] * pos[i + 1] for i in range(0, len(pos) - 1, 2))
ans += sum(neg[i] * neg[i + 1] for i in range(0, len(neg) - 1, 2))
print(ans)