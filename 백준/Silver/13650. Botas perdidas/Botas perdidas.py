while True:
    try:
        E = [0] * 31
        D = [0] * 31
        for _ in range(int(input())):
            M, L = input().split()
            M = int(M) - 30
            if L == 'E':
                E[M] += 1
            else:
                D[M] += 1
        print(sum(min(a, b) for a, b in zip(E, D)))
            
    except:
        break