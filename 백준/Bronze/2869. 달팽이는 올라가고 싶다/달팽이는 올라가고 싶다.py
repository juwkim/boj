import math
A, B, V = map(int, input().split())
print(math.ceil((V - B) / (A - B)))