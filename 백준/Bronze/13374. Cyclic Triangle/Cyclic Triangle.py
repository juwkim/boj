g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, Q = g()
    for _ in range(Q):
        R, C = g()
        if R == 0:
            print((C + 1) % 10)
        else:
            num = N % 10
            x, y, d = 0, N - 1, 1
            for cur in range(N - 1, -1, -1):
                if d == 0:
                    if x == R:
                        print((num + C - y) % 10)
                        break
                    else:
                        y += cur
                elif d == 1:
                    if y == C:
                        print((num + R - x) % 10)
                        break
                    else:
                        x += cur
                else:
                    if R - C == x - y:
                        print((num + x - R) % 10)
                        break
                    else:
                        x -= cur
                        y -= cur
                d = (d + 1) % 3
                num = (num + cur) % 10