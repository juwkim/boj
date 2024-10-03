s = input()
h, v = 0, 0
for c in input():
    match c:
        case 'h': h ^= 1
        case 'v': v ^= 1
        case _: h ^= 1; v ^= 1
if h and v:
    t = "qpdb"
    s = reversed(s)
elif h:
    t = "dbqp"
    s = reversed(s)
elif v:
    t = "pqbd"
else:
    t = "bdpq"
d = {k: v for k, v in zip("bdpq", t)}
print(*[d[c] for c in s], sep='')