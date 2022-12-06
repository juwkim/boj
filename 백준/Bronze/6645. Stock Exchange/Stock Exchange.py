while (s:= input()) != '0 END':
    n, issuer = s.split()
    n = int(n)
    names = []
    buy = dict()
    sell = dict()
    for _ in range(n):
        name, Type, cost = input().split()
        names.append([name])
        if Type == 'buy':
            buy[name] = float(cost)
        else:
            sell[name] = float(cost)
            
    for i in range(n):
        if buy.get(names[i][0]):
            cost = buy.get(names[i][0])
            for k, v in sell.items():
                if v <= cost:
                    names[i].append(k)
        else:
            cost = sell.get(names[i][0])
            for k, v in buy.items():
                if v >= cost:
                    names[i].append(k)
    print(issuer)
    for l in names:
        name, *other = l
        if other:
            print(f'{name}:', *other)
        else:
            print(f'{name}: NO-ONE')