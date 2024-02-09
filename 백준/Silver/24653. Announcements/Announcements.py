N, *S, T = map(int, open(0).read().split())
check = set()
for num in S:
    check.add(num // T)
print(len(check))