import sys
input = sys.stdin.readline

tc = 1
while True:
    H, V, h, v = map(float, input().split())
    if H == 0:
        break
    n = int(input())
    print(f"Case {tc}:")
    for _ in range(n):
        x, y = map(float, input().split())
        color = 0
        X0, Y0 = 0, 0
        W, Ht = H, V
        while True:
            WL, HB = h * W, v * Ht
            if x < X0 + WL and y > Y0 + HB or x > X0 + WL and y < Y0 + HB:
                break
            color ^= 1
            if x < X0 + WL and y < Y0 + HB:
                W, Ht = WL, HB
            else:
                W, Ht = (1 - h) * W, (1 - v) * Ht
                X0 += WL
                Y0 += HB
        print(("black", "white")[color])
    tc += 1