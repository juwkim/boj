for i in range(1, 1+int(input())):
    n = int(input())
    count, j = 0, 0
    names = [input() for _ in range(n)]
    for name in sorted(names):
        if name != names[j]:
            count += 1
            names.remove(name)
        else:
            j += 1
    print(f'Case #{i}: {count}')