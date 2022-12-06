import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

step = 1
while (s:= g())[0]:
    print('Case', step)
    n, k1, k2 = s
    nums = g()
    buf = [*range(1, 1+n)]
    buf.sort(key=lambda x: (nums[x-1], x))
    print(*sorted(buf[:k1]))
    print(*sorted(buf[-k2:], reverse=True))
    step += 1