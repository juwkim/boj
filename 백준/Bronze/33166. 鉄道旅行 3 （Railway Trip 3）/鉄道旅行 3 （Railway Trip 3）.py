P, Q, A, B = map(int, open(0).read().split())
if Q > P:
    print(P * A + (Q - P) * B)
else:
    print(Q * A)