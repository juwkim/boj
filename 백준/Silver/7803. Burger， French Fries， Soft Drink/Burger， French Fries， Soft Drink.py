from math import comb
while True:
    try:
        n, l = input().split()
        n = int(n)
        ans = 'Impossible'
        a, b, c = 0, 0, 0
        cnt = 0
        if len(l) % 3 == 0 and len(l) >= n * 3:
            for p in l:
                if p == 'B':
                    a += 1
                elif p == 'F':
                    b += 1
                else:
                    c += 1
                if a and a == b == c:
                    cnt += 1
                    a, b, c = 0, 0, 0
        if a == b == c == 0 and cnt >= n:
            ans = comb(cnt-1, n-1)
        print(ans)
    except:
        break