A, B, C = map(int, input().split())
W = A * 7 + B
print(7 * (C // W) - (-(C % W) // A))