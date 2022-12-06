fi = lambda: [*map(float, input().split())]
p = [fi() for _ in range(int(input()))]
for _ in range(int(input())):
    n = int(input())
    nums = [*map(int, input().split())]
    ans = 0
    for i in range(n-1):
        x1, y1 = p[nums[i]]
        x2, y2 = p[nums[i+1]]
        ans += ((x1 - x2) ** 2 + (y1 - y2) ** 2) **.5
    print(round(ans))