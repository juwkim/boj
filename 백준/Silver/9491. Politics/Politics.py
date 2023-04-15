while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    idx = {input(): i for i in range(n)}
    
    supporter_list = [[] for _ in range(n)]
    cur = n
    for _ in range(m):
        name, candidate = input().split()
        if candidate in idx:
            supporter_list[idx[candidate]].append(name)
        else:
            idx[candidate] = cur
            cur += 1
            supporter_list.append([name])
    for supporter in supporter_list:
        if supporter:
            print(*supporter, sep='\n')