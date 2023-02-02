def g(): return [*map(int, input().split())]

while (s:= input()) != '0':
    D, M = map(int, s.split())
    P = g()
    
    ans = 0
    Min, Max = P[0], P[0]
    for i in range(1, D):
        if P[i] > Max:
            Max = P[i]
            ans = max(ans, M // Min * (Max - Min))
        elif P[i] < Min:
            Min, Max = P[i], P[i]
    print(ans)