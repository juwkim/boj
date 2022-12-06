for _ in range(int(input())):
    cnt = 0
    num = int(input())
    while num >= 10:
        num = str(num)
        num = max(int(num[:i]) * int(num[i:]) for i in range(1, len(num)))
        cnt += 1
    print(cnt)