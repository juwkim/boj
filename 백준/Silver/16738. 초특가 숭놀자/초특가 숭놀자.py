N, Q = map(int, input().split())
Map = bytearray(N)
time = 1
dic = {}
for _ in range(Q):
    cmd, a, b = input().split()
    a, b = int(a), int(b)
    if cmd == 'new':
        l, r = 0, 0
        while r < N:
            if Map[r]:
                l = r + 1
            else:
                if r - l + 1 >= b:
                    break
            r += 1
        if r == N:
            print('REJECTED')
        else:
            for i in range(l, r + 1):
                Map[i] = 1
            dic[time] = [a, l, r]
            time += 1
            print(l + 1, r + 1)
    elif cmd == 'in':
        dic[a][0] += b
    else:
        dic[a][0] -= b
        if dic[a][0] == 0:
            _, l, r = dic[a]
            for i in range(l, r + 1):
                Map[i] = 0
            print('CLEAN', l + 1, r + 1)