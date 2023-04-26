def get_round(num):
    
    r = 0
    while r < 30 and num:
        q, num = divmod(num * 3, 1)
        if q == 1:
            return r
        r += 1
    return r

for case in range(1, 1 + int(input())):
    
    N = int(input())
    buf = []
    for _ in range(N):
        s = input()
        buf.append((get_round(float(s)), float(s), s))
    
    print(f'Case #{case}:')
    for r, _, num in sorted(buf):
        print(num)