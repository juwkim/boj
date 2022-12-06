g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n = int(input())
    a = [g() + [-1] for _ in range(n)] + [[-1] * (n + 1)]
    flag = 'NO'
    for i in range(n):
        for j in range(n):
            if a[i][j] in [0, a[i][j+1], a[i+1][j]]:
                flag = 'YES'
                break
    print(flag)