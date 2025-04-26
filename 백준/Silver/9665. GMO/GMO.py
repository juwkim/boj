apple = [*map("ACGT".index, input())]
pig = [*map("ACGT".index, input())]
cost = [*map(int, input().split())]
ans = sum(cost[x] for x in pig)
for i in range(len(apple)):
    cur, j = 0, i
    for c in pig:
        if j < len(apple) and c == apple[j]:
            j += 1
        else:
            cur += cost[c]
    ans = min(ans, cur)
print(ans)