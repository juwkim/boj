for _ in range(int(input())):
    n = int(input())
    factors, i = [], 2
    cur = n
    while i * i <= n:
        while cur % i == 0:
            cur //= i
            factors.append(i)
        i += 1
    if factors:
        print(f"{n}:", *factors, cur if cur != 1 else "")
    else:
        print(f"{n}: prime")