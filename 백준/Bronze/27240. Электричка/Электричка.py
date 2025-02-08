n, a, b, *l = map(int, open(0).read().split())
s, t = sorted(l)
if a < s and t < b:
    print("City")
elif t <= a or s >= b:
    print("Outside")
else:
    print("Full")