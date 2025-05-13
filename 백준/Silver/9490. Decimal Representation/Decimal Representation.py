import sys
input = sys.stdin.readline

def solve(a, b):
    q, r = divmod(a, b)
    ret = len(str(q))
    if r == 0:
        return ret
    check = bytearray(b)
    while r and not check[r]:
        check[r] = 1
        q, r = divmod(r * 10, b)
        ret += len(str(q))
    if check[r]:
        return ret + 3
    return ret + 1

a = [[0] * 501 for _ in range(501)]
for i in range(500):
    for j in range(500):
        a[i+1][j+1] = max(a[i][j+1], a[i+1][j], solve(i+1, j+1))
while n:=int(input()):
    print(a[n][n])