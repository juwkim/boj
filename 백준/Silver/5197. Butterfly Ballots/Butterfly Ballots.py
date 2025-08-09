import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    n = int(input())
    me, *v = [int(input()) for _ in range(n)]
    ans = "Possible"
    if n >= 3:
        v.sort()
        me += v[-1] >> 1
        cur = v[-1] >> 1
        v.pop()
        while v:
            idx = -1
            while idx + 1 < len(v) and cur + v[idx + 1] // 2 <= me:
                idx += 1
            if idx == -1:
                ans = "Impossible"
                break
            cur = v[idx] // 2
            v.pop(idx)
    print(f"Data Set {tc}:\n{ans}")