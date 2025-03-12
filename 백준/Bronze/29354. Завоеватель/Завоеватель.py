n, *t = map(int, open(0).read().split())
Min, Sum = 1e9, 0
for num in t:
    Min = min(Min, num)
    Sum += Min
print(Sum - Min)