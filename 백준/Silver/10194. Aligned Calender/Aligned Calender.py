g = lambda: map(int, input().split())

def is_leaf(year):
    return not year % 4 and (year % 100 or not year % 400)

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(int(input())):
    y, m, d = g()
    
    t = d
    for i in range(m-1):
        if i == 1 and is_leaf(y):
            t += 29
        else:
            t += days[i]
    if t > 364:
        ans = 'a HOLIDAY'
    else:
        a, b = divmod(t-1, 28)
        ans = f'{y}/{a+1}/{b+1}'
    print(f'{y}/{m}/{d} became {ans}')