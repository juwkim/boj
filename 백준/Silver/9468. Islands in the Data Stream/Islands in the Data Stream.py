g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    num, *l = g()   
    ans = sum(i < j for i, j in zip(l, l[1:]))
    print(num, ans)