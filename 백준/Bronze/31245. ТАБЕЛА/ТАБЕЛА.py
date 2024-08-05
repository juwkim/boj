a, b, c = input().split()
if a[1] == b[0]:
    b = "'" + b[1]
if b[1] == c[0]:
    c = "'" + c[1]
print(a + b + c)