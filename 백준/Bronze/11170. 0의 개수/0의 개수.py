for _ in range(int(input())):
    N, M = map(int, input().split())
    cnt = 0
    for i in map(str, range(N, M+1)):
        cnt += i.count('0')
    print(cnt)