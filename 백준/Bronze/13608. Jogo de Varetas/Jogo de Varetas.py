while n:= int(input()):
    cnt = 0
    for _ in range(n):
        cnt += int(input().split()[1]) >> 1
    print(cnt >> 1)