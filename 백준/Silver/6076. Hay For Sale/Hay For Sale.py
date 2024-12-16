C, H, *V = map(int, open(0).read().split())
s = set()
for num in V:
    s.update([a + num for a in s if a + num <= C])
    if num <= C: s.add(num)
    if C in s: break
print(max(s))