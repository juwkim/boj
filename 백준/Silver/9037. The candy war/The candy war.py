g = lambda: [*map(int, input().split())]


for _ in range(int(input())):
    N = int(input())
    candy = g()
    for i in range(N):
        if candy[i] & 1:
            candy[i] += 1
    cnt = 0
    while len(set(candy)) != 1:
        tmp = [stu//2 for stu in candy]
        for i in range(1, N):
            candy[i] += tmp[i-1]
        candy[0] += tmp[-1]
        for i in range(N):
            candy[i] -= tmp[i]
            candy[i] += candy[i] & 1
        cnt += 1
    print(cnt)