def get(te):
    if ord('0') <= ord(te) <= ord('9'):
        return ord(te) - ord('0')
    else:
        return ord(te) - ord('A') + 10
 
A, B = input(), input()
a, b, c = [], [], []
n = len(A)//2
for i in range(n):
    a.append(16 * get(A[2*i]) + get(A[2*i+1]))
for i in range(n+1):
    b.append(16 * get(B[2*i]) + get(B[2*i+1]))

c.append(ord(' ')^b[0])
for i in range(1, n+1):
    c.append(c[i-1]^a[i-1]^b[i])

for i in range(n+1):
    print('%X%X' % (divmod(c[i], 16)), end='')