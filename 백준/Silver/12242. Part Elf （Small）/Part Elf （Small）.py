for tc in range(1, 1 + int(input())):
    a, b = map(int, input().split('/'))
    if b & b - 1:
        ans = 'impossible'
    else:
        ans, p = 1, 2 * a
        while p < b:
            ans += 1
            p <<= 1
    print(f"Case #{tc}: {ans}")