res = [0, 1]
a, b = res
for i in range(9999):
    a, b = b, a + b
    res.append(b)

for i in range(1, 1 + int(input())):
    P, Q = map(int, input().split())
    print(f'Case #{i}:', res[P] % Q)