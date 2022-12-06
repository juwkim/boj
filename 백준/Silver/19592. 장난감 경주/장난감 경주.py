g = lambda: [*map(int, input().split())]


for _ in range(int(input())):
    N, X, Y = g()
    V = g()
    
    Max_speed = max(V[:-1])
    My_speed = V[-1]
    time = X / Max_speed
    if My_speed > Max_speed:
        print(0)
    elif 1 + (X - Y) / My_speed >= time:
        print(-1)
    else:
        l, r = 0, Y
        while l <= r:
            middle = (l + r) // 2
            my_time = 1 + (X - middle) / My_speed
            
            if my_time >= time:
                l = middle + 1
            else:
                r = middle - 1
        print(l)