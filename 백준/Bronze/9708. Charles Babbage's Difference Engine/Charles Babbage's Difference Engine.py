g = lambda: [*map(int, input().split())]

nums = [[1],[-49,50],[1176,-2400,1225],[-18424,56400,-57575,19600]]

a = [[0] * 51 for _ in range(7)]
for p in range(1, 1 + int(input())):
    n, *l = g()
    # if n < 4:
    #     ans = sum(i * j for i, j in zip(nums[n], l))
    # else:
    a[0][:n+1] = l
    for i in range(1, n+1):
        for j in range(n+1-i):
            a[i][j] = a[i-1][j+1] - a[i-1][j]
    a[n+1] = [0] * 51
    for i in range(50-n):
        for j in range(n+1):
            a[n-j][i+j+1] = a[n-j][i+j] + a[n-j+1][i+j]
    ans = a[0][50]
    print(f'Case #{p}:', ans)