while x:=int(input()):
    S, P, C = input(), input(), input()
    n = len(C)
    d = int(n ** 1.5 + x) % n
    s_pos = {c: i for i, c in enumerate(S)}
    M = [None] * n
    M[d] = P[s_pos[C[d]]]
    for j in range(n - 1):
        a = s_pos[C[d - 1 - j]]
        b = s_pos[M[(d - j) % n]]
        M[d - 1 - j] = P[a ^ b]
    print(''.join(M))