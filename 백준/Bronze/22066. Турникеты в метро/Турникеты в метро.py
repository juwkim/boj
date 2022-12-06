import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    *l, k = g()
    a, b = sorted(l)
    ans = -1
    if a < 100 and b < 100:
        for i in range(a):
            if (b - i) == (a - i) * k:
                ans = i
                break
    elif a >= 100:
        if k == 1:
            ans = 0
        else:
            tmp = a - 99
            a -= tmp
            b -= tmp
            for i in range(a):
                if min(99, b - i) == (a - i) * k:
                    ans = tmp + i
                    break         
    else:
        for i in range(a):
            if min(99, b - i) == (a - i) * k:
                ans = i
                break 
    print(ans)