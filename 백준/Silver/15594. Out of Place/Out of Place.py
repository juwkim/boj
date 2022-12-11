N = int(input())
s = [int(input()) for _ in range(N)]
t = sorted(s)
ans = set()
for a, b in zip(s, t):
    if a != b:
        ans.add(a)
        ans.add(b)
if ans:
    print(len(ans) - 1)
else:
    print(0)