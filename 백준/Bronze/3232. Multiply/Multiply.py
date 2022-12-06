for _ in range(int(input())):
    s = input()
    p, q, r = s.split()
    start = int(max(s)) + 1
    ans = 0
    for i in range(start, 17):
        if int(p, i) * int(q, i) == int(r, i):
            ans = i
            break
    print(ans)