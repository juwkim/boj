s = input()
h, v = 0, 0
for c in input():
    match c:
        case 'h':
            h ^= 1
        case 'v':
            v ^= 1
        case _:
            h ^= 1
            v ^= 1
if h and v:
    d = {k: v for k, v in zip("bdpq", "qpdb")}
    s = s[::-1]
elif h:
    d = {k: v for k, v in zip("bdpq", "dbqp")}
    s = s[::-1]
elif v:
    d = {k: v for k, v in zip("bdpq", "pqbd")}
else:
    d = {k: v for k, v in zip("bdpq", "bdpq")}
print(*[d[c] for c in s], sep='')