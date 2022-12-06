s = [*map(sorted, zip(*[[*map(int, input().split())] for _ in range(int(input()))]))]
tt = max(s, key=lambda x: (sum(x), x.count(3), x.count(2)))
print(s.index(tt) + 1 if s.count(tt) == 1 else 0, sum(tt))