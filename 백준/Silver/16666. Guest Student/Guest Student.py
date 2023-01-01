for _ in range(int(input())):
    k = int(input())
    a = [*map(int, input().split())]
    week_sum = sum(a)
    week, remain = divmod(k - 1, week_sum)
    
    remain += 1
    a += a
    day = 1
    while not any(sum(a[i:i+day]) == remain for i in range(7)):
        day += 1
    print(week * 7 + day)