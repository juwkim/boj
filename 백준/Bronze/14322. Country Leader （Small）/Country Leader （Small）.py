for cnt in range(1, 1 + int(input())):
    names = [input() for _ in range(int(input()))]
    name = min(names, key=lambda x: (-len(set(x)), x))
    print(f'Case #{cnt}: {name}')