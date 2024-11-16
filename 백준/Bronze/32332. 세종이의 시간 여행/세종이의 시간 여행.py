def get():
    Y, M, D, T, P = input().split()
    return int(Y), int(M) - 1, int(D) - 1, float(T), float(P)

Y0, M0, D0, T0, P0 = get()
Y1, M1, D1, T1, P1 = get()
a = 2 * (Y0 * 360 + M0 * 30 + D0) - (Y1 * 360 + M1 * 30 + D1)
Y, M, D, T, P = a // 360, a % 360 // 30 + 1, a % 360 % 30 + 1, 2 * T0 - T1, 2 * P0 - P1
print(f"{Y} {M} {D} {T:.3f} {P:.3f}")