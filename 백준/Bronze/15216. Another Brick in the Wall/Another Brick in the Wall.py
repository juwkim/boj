g = lambda: [*map(int, input().split())]
h, w, n = g()
cur = 0
flag = 'NO'
for num in g():
    if cur > w:
        flag ='NO'
        break
    elif cur == w:
        h -= 1
        cur = num
        if h == 0:
            flag = 'YES'
            break
    else:
        cur += num
if cur == w and h == 1:
    flag = 'YES'    
print(flag)