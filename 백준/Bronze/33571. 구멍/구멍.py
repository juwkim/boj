d = {c: 1 for c in "ADOPQRabdegopq@"}
d['B'] = 2
print(sum(d.get(c, 0) for c in input()))