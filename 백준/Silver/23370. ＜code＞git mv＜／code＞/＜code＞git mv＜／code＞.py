src = input().split('/')
dst = input().split('/')

l = min(len(src), len(dst))
i, j = 0, 0
while i < l and src[i] == dst[i]: i += 1
while i + j < l and src[-1 - j] == dst[-1 - j]: j += 1

A = '/'.join(src[:i])
B = '/'.join(src[i:len(src) - j])
C = '/'.join(dst[i:len(dst) - j])
D = '/'.join(src[len(src) - j:])

if A and not A.endswith('/'):
    A += '/'
if D and not D.startswith('/'):
    D = '/' + D
print(f"{A}{{{B} => {C}}}{D}")