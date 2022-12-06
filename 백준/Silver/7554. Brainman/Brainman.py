g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    n, *l = g()
    ans = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                ans += 1
                l[j], l[j+1] = l[j+1], l[j]
    print(f'Scenario #{_}:\n{ans}\n')