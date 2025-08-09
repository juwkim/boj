import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    n = int(input())
    me = int(input())
    ans = "Possible"
    if n > 1:
        *v, cur = sorted(int(input()) >> 1 for _ in range(n - 1))
        me += cur
        while v:
            idx = -1
            while idx + 1 < len(v) and cur + v[idx + 1] <= me:
                idx += 1
            if idx == -1:
                ans = "Impossible"
                break
            cur = v.pop(idx)
    print(f"Data Set {tc}:\n{ans}")