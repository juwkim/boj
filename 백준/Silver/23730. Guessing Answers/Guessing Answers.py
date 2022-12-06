g = lambda: [*map(int, input().split())]


N, M = g()
nums = g()

solved = [0] * N
for good in g():
    solved[good-1] = nums[good-1]

for i in range(N):
    if solved[i] == 0:
        if i == 0:
            check = set(range(1, 6))
            check.remove(nums[i])
            if i != N - 1 and solved[i+1] in check:
                check.remove(solved[i+1])
            solved[i] = check.pop()
        elif i == N-1:
            check = set(range(1, 6))
            check.remove(nums[i])
            if i != 0 and solved[i-1] in check:
                check.remove(solved[i-1])
            solved[i] = check.pop()
        else:
            check = set(range(1, 6))
            check.remove(nums[i])
            if solved[i-1] in check:
                check.remove(solved[i-1])
            if solved[i+1] in check:
                check.remove(solved[i+1])
            solved[i] = check.pop()            
print(*solved)