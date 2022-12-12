n = int(input())
Map = [[*input()] for _ in range(n)]
To = [[*input()] for _ in range(n)]
ans = 1e9
for i in range(4):
    cnt = sum(sum(s != t for s, t in zip(a, b)) for a, b in zip(Map, To))
    ans = min(ans, cnt + min(i, 4 - i))
    Map = [l[::-1] for l in zip(*Map)]
print(ans)