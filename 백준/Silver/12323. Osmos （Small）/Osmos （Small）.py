g = lambda: [*map(int, input().split())]
for tc in range(1, 1 + int(input())):
    A, N = g()
    ans, cur = 1e9, 0
    for i, mote in enumerate(sorted(g())):
        if A == 1:
            cur += N - i
            break
        if mote < A:
            A += mote
        else:
            ans = min(ans, cur + N - i)
            while mote >= A:
                A += A - 1
                cur += 1
            A += mote
    ans = min(ans, cur)
    print(f"Case #{tc}: {ans}")