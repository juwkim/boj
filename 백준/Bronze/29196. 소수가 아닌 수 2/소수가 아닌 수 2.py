a, b = input().split('.')
q = pow(10, len(b))
p = int(a) * q + int(b)
print("YES")
print(p, q)