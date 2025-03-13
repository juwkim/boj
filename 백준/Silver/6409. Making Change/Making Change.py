import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product

5, 10, 20, 50, 100, 200

while (s:=input()) != "0 0 0 0 0 0":
    *l, num = s.split()
    a, b, c, d, e, f = map(int, l)
    num = int(float(num) * 100)
    ans = 1e9
    for t1, t2, t3, t4, t5, t6 in product(range(min(a, num // 5 + 1) + 1), range(min(b, num // 10 + 1) + 1), range(min(c, num // 20 + 1) + 1), range(min(d, num // 50 + 1) + 1), range(min(e, num // 100 + 1) + 1), range(min(f, num // 200 + 1) + 1)):
        toss = 5 * t1 + 10 * t2 + 20 * t3 + 50 * t4 + 100 * t5 + 200 * t6
        change = toss - num
        if change < 0:
            continue
        c6, change = divmod(change, 200)
        c5, change = divmod(change, 100)
        c4, change = divmod(change, 50)
        c3, change = divmod(change, 20)
        c2, change = divmod(change, 10)
        c1 = change // 5
        ans = min(ans, t1 + t2 + t3 + t4 + t5 + t6 + c1 + c2 + c3 + c4 + c5 + c6)    
    print(f"{ans: 3d}")