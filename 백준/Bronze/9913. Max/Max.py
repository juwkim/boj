import statistics as s
a = s.Counter([input() for _ in range(int(input()))])
print(max(a.values()))