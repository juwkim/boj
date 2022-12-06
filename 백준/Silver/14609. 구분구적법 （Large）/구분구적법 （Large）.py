g = lambda: [*map(int, input().split())]

K = int(input())
c = g()[::-1]
a, b, N = g()
dx = (b - a) / N

real = 0
for i in range(K+1):
    real += c[i] * (pow(b, i + 1) - pow(a, i + 1)) / (i + 1)

def f(k, e):
    x = a + k * dx + e
    
    val = 0
    mult = 1
    for i in range(K+1):
        val += mult * c[i]
        mult *= x
    return val

def f_sum(e):
    ret = 0
    for k in range(N):
        ret += f(k, e) * dx
    return ret


l, r = 0, dx
if f_sum(l) > real:
    print(-1)
elif f_sum(r) < real:
    print(-1)
else:
    while True:
        m = (l + r) / 2
        f_val = f_sum(m)
        
        if abs(f_val - real) <= 1e-4:
            print(m)
            break
        elif f_val > real + 1e-4:
            r = m
        else:
            l = m