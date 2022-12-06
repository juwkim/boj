while (s:= input()) != '0':
    n, msg = s.split()
    n = int(n)
    Set = set()
    left = set()
    ans = 0
    for c in msg:
        if c in Set:
            Set.remove(c)
        elif c in left:
            left.remove(c)
        elif len(Set) < n:
            Set.add(c)
        else:
            ans += 1
            left.add(c)
    if ans:
        print(ans, 'customer(s) walked away.')
    else:
        print('All customers tanned successfully.')