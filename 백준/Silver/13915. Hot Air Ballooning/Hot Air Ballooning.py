while True:
    try:
        N = int(input())
        s = set()
        for _ in range(N):
            s.add(tuple(sorted(set(input()))))
        print(len(s))
    except:
        break