import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(lambda x: int(x) - 201, input().split())
    din, dout = (b - a) % 43, (a - b) % 43
    if din < dout:
        print("Inner circle line")
    elif din > dout:
        print("Outer circle line")
    else:
        print("Same")