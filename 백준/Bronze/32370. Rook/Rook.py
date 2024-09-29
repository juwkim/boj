a, b, x, y = map(int, open(0).read().split())
if a and b:
    print(2)
elif (a == 0 and x == 0 and y < b) or (b == 0 and y == 0 and x < a):
    print(3)
else:
    print(1)