L, H = map(int, input().split())
count = 0
for i in range(L, H+1):
    k = set(str(i))
    if '0' not in k and len(k) == 6 and all(i % int(t) == 0 for t in k):
        count += 1
print(count)