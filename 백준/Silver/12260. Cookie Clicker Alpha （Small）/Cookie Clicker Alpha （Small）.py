for step in range(1, 1 + int(input())):
    C, F, X = map(float, input().split())
    V_max = F * (X - C) / C
    ans, V = 0, 2
    ans = 0
    while V < V_max:
        ans += C / V
        V += F
    ans += X / V
    print(f'Case #{step}: {ans}')