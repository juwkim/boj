import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

MOD = 1000002013
cost = lambda d: (d * N - d * (d - 1) // 2) % MOD

for tc in range(1, int(input()) + 1):
    N, M = g()
    ans, events = 0, []
    for _ in range(M):
        o, e, p = g()
        ans = (ans + cost(e - o) * p) % MOD
        events.extend(((o, -p), (e, p)))    
    st = []
    for station, cnt in sorted(events):
        if cnt < 0:
            st.append((station, -cnt))
        else:
            need = cnt
            while need:
                o_st, cnt = st.pop()
                used = min(cnt, need)
                ans = (ans - cost(station - o_st) * used) % MOD
                cnt -= used
                need -= used
                if cnt:
                    st.append((o_st, cnt))
    print(f"Case #{tc}: {ans}")