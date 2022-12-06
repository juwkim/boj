costs = {'bo': 0, 'et': 50, 'ke': 50, 'so': 0, 'ta': 50}

N = int(input())
nations = [input()[:2] for _ in range(N)]

total, i = 0, 0
while i < N:
    try:
        total += costs[nations[i]]
        i += 1
    except:
        if nations[i] == 'na':
            total += 40 + ('so' not in nations[:i]) * 100
            i += 1
        else:
            if i + 1 != N and nations[i+1][0] == 'z':
                total += 50
                i += 2
            elif nations[i] == 'za':
                total += 50
                i += 1
            else:
                total += 30
                i += 1
    
print(total)