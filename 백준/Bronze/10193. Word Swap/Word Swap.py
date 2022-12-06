for _ in range(int(input())):
    s, t = input().split()
    p = sum(ord(a) - ord(b) for a, b in zip(s, t))
    if p:
        print(f'Swapping letters to make {s} look like {t} {["cost","earned"][p>0]} {abs(p)} coins.')
    else:
        print(f'Swapping letters to make {s} look like {t} was FREE.')