a, b = zip(*[l.split() for l in open(0)])
print(a[max(range(7), key=lambda i: int(b[i]))])