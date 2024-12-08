for _ in range(int(input())):
    A, B, C = map(int, input().split())
    ans = "No"
    if C:
        if A >= C and (A - C) % 2 == 0:
            ans = "Yes"
    elif B & 1:
        if A >= 2 and A % 2 == 0:
            ans = "Yes"
    elif A % 2 == 0:
        ans = "Yes"
    print(ans)