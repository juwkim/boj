input()
for N in [*map(int, input().split())]:
    m, n = divmod(N, 21)
    x = m * (189*m + 21) // 2
    s, t = n//3, n//7 
    y = s * (s + 1) // 2 * 3 + s * m * 21
    z = t * (t + 1) // 2 * 7 + t * m * 21
    print(x + y + z)