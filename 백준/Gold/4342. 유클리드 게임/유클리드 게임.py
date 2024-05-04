while True:
    A, B = sorted(map(int, input().split()))
    if A == 0: break
    i = 0
    while B % A and B // A == 1:
        A, B = B - A, A
        i ^= 1
    print("AB"[i], "wins")