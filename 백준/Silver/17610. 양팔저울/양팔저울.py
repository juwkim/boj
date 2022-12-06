def solve(idx, cumulativeSum):
    if idx == k:
        if cumulativeSum > 0:
            check.add(cumulativeSum)
        return
        
    solve(idx + 1, cumulativeSum - weightList[idx])
    solve(idx + 1, cumulativeSum + weightList[idx])
    solve(idx + 1, cumulativeSum)

k = int(input())
weightList = [*map(int, input().split())]
check = set()

solve(0, 0)
print(sum(weightList) - len(check))