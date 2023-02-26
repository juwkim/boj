def g(): return [*map(int, input().split())]

N, M = g()
buf = sorted([g() for _ in range(N)], reverse=True)[:M]
dot = sum(num[0] for num in buf)
time = min(num[1] for num in buf)
print(dot, time)