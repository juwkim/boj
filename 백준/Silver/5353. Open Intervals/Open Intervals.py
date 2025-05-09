import sys
input = sys.stdin.readline

while n:=int(input()):
    intervals = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: x[1])
    ans = 0
    last_end = -1
    for start, end in intervals:
        if start >= last_end:
            ans += 1
            last_end = end
    print(ans)