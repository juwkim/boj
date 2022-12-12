for _ in range(3):
    x, y = input().split()
    x = [int(i) for i in x]
    y = [int(i) for i in y]
    ans = 'nothing'
    if set(x) == set(y):
        ans = 'friends'
    else:
        for i in range(len(x) - 1):
            x[i], x[i+1] = x[i] + 1, x[i+1] - 1
            if set(x) == set(y):
                ans = 'almost friends'
                break
            x[i], x[i+1] = x[i] - 2, x[i+1] + 2
            if (i != 0 or x[i]) and set(x) == set(y):
                ans = 'almost friends'
                break
            x[i], x[i+1] = x[i] + 1, x[i+1] - 1
        
        x, y = y, x
        for i in range(len(x) - 1):
            x[i], x[i+1] = x[i] + 1, x[i+1] - 1
            if set(x) == set(y):
                ans = 'almost friends'
                break
            x[i], x[i+1] = x[i] - 2, x[i+1] + 2
            if (i != 0 or x[i]) and set(x) == set(y):
                ans = 'almost friends'
                break
            x[i], x[i+1] = x[i] + 1, x[i+1] - 1            
    print(ans)