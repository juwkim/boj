g = lambda: [*map(int, input().split())]

NR, NC = g()
ans = 0
x, y = 0, 0
nums = [g() for _ in range(NR)]
for i in range(NR-2):
    for j in range(NC-2):
        tmp = sum(nums[p][q] for p in range(i, i+3) for q in range(j, j+3))
        if tmp > ans:
            ans = tmp
            x, y = i, j
print(ans)
print(x+1, y+1)