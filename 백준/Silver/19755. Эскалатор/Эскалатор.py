def solve(n):
    if n == 1:
        ans = 1
    elif n < 10:
        ans = 2
    elif n < 100:
        ans = 3
        comp = 10
        while comp < n:
            ans += 2
            comp += 10
    else:
        ans = 1
        i = 2
        comp = 100
        while n >= comp:
            ans += i * comp * 9 // 100
            i += 1
            comp *= 10
        p = n - n % 10
        
        ans += i * ((p - comp // 10) // 10 + 1)
        if n % 10:
            ans += i
    return ans

print(solve(int(input())))