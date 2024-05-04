while True:
    A, B = sorted(map(int, input().split()))
    if A == B == 0:
        break
    turn = 0
    while True:
        q, r = divmod(B, A)
        if r == 0 or q > 1:
            break
        A, B = B - A, A
        turn ^= 1
    print("AB"[turn], "wins")