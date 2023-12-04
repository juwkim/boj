for _ in range(int(input())):
    q, r = divmod(int(input()), 5)
    ans = ["++++" for _ in range(q)] + ["|" * r]
    print(*ans)