L, R = input().split()
a = sum(map(int, L)) % 9
b = sum(map(int, R)) % 9
if a <= b:
    print(sum(range(a, b+1)) % 9)
else:
    print((-sum(range(b+1, a))) % 9)