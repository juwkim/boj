g = lambda: [*map(int, input().split())]
while (s:= g()) != [0, 0]:
    a, b = sorted(s)
    
    i, tot = 1, 0
    while tot < a:
        tot += i
        i += 1
    
    ans = 0
    while a < b:
        a += i
        i += 1
        ans += 1

    if (i - 2) * (i - 1) // 2 < b:
        ans += max(0, a - b - ans)
    else:
        a -= i - 1
        ans -= 1
        ans += b - a
    print(ans)