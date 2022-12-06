for j in range(1, 1 + int(input())):
    n = [*map(int, input().split()[1])]
    k = [n[0]]
    for i in range(len(n)-1):
        k.append(k[i]+n[i+1])
    count = max([i+1 - k[i] for i in range(len(n))] + [0])
    print(f'Case #{j}: {count}')