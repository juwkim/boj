from statistics import Counter
g = lambda: [*map(int, input().split())]

N = int(input())

nums = [g() for _ in range(N)]
s = Counter(map(sum, nums))

nums = [*zip(*nums)]
t = Counter(map(sum, nums))

a = sum([nums[i][i] for i in range(N)])
b = sum([nums[N-1-i][i] for i in range(N)])

ans = -1
if len(s) == 2 and s == t and a in s and b in s:
    x, y = sorted(s.keys())
    if s[x] == 1:
        ans = y - x
print(ans)