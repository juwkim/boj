import datetime as d
N, K = map(int, input().split())

def g(count, s, N, K):
    t = d.timedelta(seconds=1)
    while s < d.timedelta(hours=N+1):
        count += (str(K) in str(s))
        s += t
    return count
print(g(0, d.timedelta(seconds=0), N, K) if K else g(min(N+1, 10) * 3600, d.timedelta(hours=10), N, K))