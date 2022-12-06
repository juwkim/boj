u = {'kg':[2.2046, 'lb'], 'lb':[0.4536, 'kg'], 'l':[0.2642, 'g'], 'g':[3.7854, 'l']}
for _ in range(int(input())):
    n, d = input().split()
    print(f'{float(n)*u[d][0]:#.4f} {u[d][1]}')