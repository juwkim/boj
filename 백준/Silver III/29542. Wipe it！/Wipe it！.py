ans = []
check = set()
for c in input():
    if c in check:
        continue
    check.add(c)
    ans.append(c)
print(*ans, sep='')