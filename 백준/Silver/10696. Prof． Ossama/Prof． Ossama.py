for t in range(1, 1 + int(input())):
    N, X = input().split()
    X = int(X)
    ans = 0
    for digit in N:
        ans = (ans * 10 + int(digit)) % X
    print(f"Case {t}: {ans}")