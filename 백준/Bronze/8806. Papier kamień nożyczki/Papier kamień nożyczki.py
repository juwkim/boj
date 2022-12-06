for _ in range(int(input())):
    X1, Y1, Z1 = map(float, input().split())
    X2, Y2, Z2 = map(float, input().split())
    Adam = X1*Y2 + Y1*Z2 + Z1*X2
    Gosia = X2*Y1 + Y2*Z1 + Z2*X1
    print("ADAM" if Adam > Gosia else "GOSIA" if Adam < Gosia else "=")