from math import isqrt
for _ in range(int(input())):
    num = int(input())
    add_set = set()
    sub_set = set()
    
    ans = 'not nasty'
    for a in range(1, isqrt(num)+1):
        b, q = divmod(num, a)
        if q == 0:
            add = a + b
            sub = abs(a - b)
            if add in sub_set or sub in add_set:
                ans = 'nasty'
                break
            add_set.add(add)
            sub_set.add(sub)
    print(num, 'is', ans)