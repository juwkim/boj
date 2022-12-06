A, B, C = map(int, input().split())
W = A * 7 + B
print(C // W * 7 + min(-(-(C % W) // A), 7))