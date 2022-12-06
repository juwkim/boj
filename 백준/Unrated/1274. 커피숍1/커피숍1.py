g = lambda: [*map(int, input().split())]

a, b = g()
Sa, Sb, S = g()

if Sa < S:
    print('gg')
elif Sb < S:
    print(1)
else:
    cnt = 1
    while a <= b and cnt <= 50:
        a += (b - a) * S / Sa
        b -= b * S / Sb
        cnt += 1
    
    print('gg' if cnt == 51 else hex(cnt).upper()[2:])