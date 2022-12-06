for _ in range(int(input())):
    t = [0]*1001
    for _ in range(int(input())):
        _, a, b = input().split()
        for i in range(int(a), int(b)):
            t[i] += 1
    print(''.join([chr(s+64) for s in t if s > 0]))