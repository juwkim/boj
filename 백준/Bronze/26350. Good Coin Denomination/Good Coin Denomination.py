for _ in range(int(input())):
    n, *l = map(int, input().split())
    ans = 'Good'
    if any(b < 2 * a for a, b in zip(l, l[1:])):
        ans = 'Bad'
    print("Denominations:", *l)
    print(ans, "coin denominations!\n")