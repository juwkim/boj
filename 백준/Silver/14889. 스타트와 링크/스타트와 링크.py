g = lambda: [*map(int, input().split())]


from itertools import combinations
N = int(input())
nums = [g() for _ in range(N)]

ans = 1e9
for l in combinations(range(N), N//2):
    A, B = 0, 0
    l = list(l)
    start, link = [], []
    for i in range(N-1, -1, -1):
        if l and i == l[-1]:
            l.pop()
            for num in start:
                A += nums[num][i] + nums[i][num]
            
            start.append(i)
        else:
            for num in link:
                B += nums[num][i] + nums[i][num]
            link.append(i)
    
    ans = min(ans, abs(A - B))
print(ans)