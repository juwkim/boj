points = list(map(int, input().split()))
A = points[0]
B = points[1]

total = []

for i in range(1005):
    total.append(str(A//B))
    if A % B == 0:
        break
    A = (A % B) * 10

quotient = total[0]
del total[0]

decimal = ''.join(total)
final = quotient + '.' + decimal
print(final)