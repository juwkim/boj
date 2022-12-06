A, B, C = map(int, input().split())
print((C > B and 1 + A // (C - B)) or -1)