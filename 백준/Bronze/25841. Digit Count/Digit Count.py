s, e, d = map(int, input().split())
d = str(d)
print(sum(str(i).count(d) for i in range(s, e+1)))