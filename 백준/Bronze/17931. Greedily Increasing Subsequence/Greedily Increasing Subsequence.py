g = lambda: [*map(int, input().split())]

n = int(input())
res = [-1]
for num in g():
    if num > res[-1]:
        res.append(num)
print(len(res) - 1)
print(*res[1:])