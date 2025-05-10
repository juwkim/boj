import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    D, K, S, *stations = map(int, input().split())
    stations = [0] + stations + [D]
    ans, cur = [], 0
    while cur < len(stations) - 1:
        nxt = cur
        while nxt + 1 < len(stations) and stations[nxt + 1] - stations[cur] <= K:
            nxt += 1
        if nxt == cur:
            print(f"Case #{tc}: out of petrol")
            break
        ans.append(stations[nxt])
        cur = nxt
    else:
        print(f"Case #{tc}:", *ans[:-1])