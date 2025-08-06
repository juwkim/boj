import sys
input = sys.stdin.readline

def build_rmq_max(a):
    n = len(a)
    log = [0] * (n + 1)
    for i in range(2, n + 1):
        log[i] = log[i >> 1] + 1
    K = log[n] + 1
    st = [a[:]]
    for j in range(1, K):
        prev = st[j - 1]
        cur = [0] * (n - (1 << j) + 1)
        span = 1 << j - 1
        for i in range(len(cur)):
            cur[i] = max(prev[i], prev[i + span])
        st.append(cur)
    return st, log

def rmq_max(st, log, L, R):
    j = log[R - L + 1]
    return max(st[j][L], st[j][R - (1<<j) + 1])

N, M, A = map(int, input().split())
v = list(map(int, input().split()))
A -= 1
st, log = build_rmq_max(v)
ans, hA = 0, v[A]
for b in map(lambda x: int(x) - 1, input().split()):
    hb = v[b]
    low = min(A, b) + 1
    high = max(A, b) - 1
    if low > high:
        ans += 1
        continue
    mx = rmq_max(st, log, low, high)
    if mx <= min(hA, hb):
        ans += 1
print(ans)