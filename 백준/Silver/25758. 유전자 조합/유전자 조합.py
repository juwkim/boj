input()
A, B = set(), set()
ans = set()
for a, b in input().split():
    for c in A:
        ans.add(max(c, b))
    for c in B:
        ans.add(max(a, c))
    A.add(a)
    B.add(b)
print(len(ans))
print(*sorted(ans))