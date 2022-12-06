g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    L, C = g()
    target = [input() for _ in range(L)]
    
    Lm, Cm = g()
    Map = [input() for _ in range(Lm)]
    
    ans = 0
    for i in range(Lm-L+1):
        idx = -C
        while True:
            idx = Map[i].find(target[0], idx+C)
            if idx == -1:
                break
            if all(Map[j][idx:idx+C] == target[j-i] for j in range(i+1, i+L)):
                ans += 1
    print(ans)