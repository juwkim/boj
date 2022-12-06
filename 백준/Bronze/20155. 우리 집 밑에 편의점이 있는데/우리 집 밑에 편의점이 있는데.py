_, M = map(int, input().split())
s = [*map(int, input().split())]
print(max(s.count(i) for i in range(1, M+1)))