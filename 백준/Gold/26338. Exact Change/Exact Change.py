for tc in range(1, 1 + int(input())):
    input()
    ans = 0
    for M in sorted(map(int, input().split())):
        if M > ans + 1:
            break
        ans += M
    print(f"Set #{tc}: {ans + 1}\n")