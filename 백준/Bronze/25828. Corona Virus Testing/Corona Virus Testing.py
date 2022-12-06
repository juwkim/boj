g, p, t = map(int, input().split())
a = g + p * t
b = g * p
print("012"[(a > b) - (a < b)])