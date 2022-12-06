g = lambda: [*map(int, input().split())]

for step in range(1, 1 + int(input())):
    N, M = g()
    dic =  {}
    for _ in range(N):
        cnt, n_price, c_price, *name = input().split()
        dic[''.join(name).lower()] = [int(cnt), float(n_price[1:]) - float(c_price[1:])]
    
    ans = 0
    for _ in range(M):
        cnt, *name = input().split()
        name = ''.join(name).lower()
        if name in dic:
            amount, discount = dic[name]
            tmp = min(int(cnt), amount)
            dic[name][0] -= tmp
            
            ans += tmp * discount
    print(f'Data Set {step}:\n${ans:.2f}\n')