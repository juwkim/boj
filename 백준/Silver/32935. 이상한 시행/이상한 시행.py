N, *a = map(int, open(0).read().split())
print(max(sum(a), -min(a)))