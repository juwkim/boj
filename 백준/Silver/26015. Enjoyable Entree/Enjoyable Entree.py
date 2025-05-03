def mat_mult(a, b):
    return (a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]), (a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1])

def mat_pow(mat, exp):
    res = (1, 0), (0, 1)
    while exp:
        if exp & 1:
            res = mat_mult(mat, res)
        mat = mat_mult(mat, mat)
        exp >>= 1
    return res

n = int(input())
if n == 1:
    print(100, 0)
elif n == 2:
    print(0, 100)
else:
    (tau, pi), _ = mat_pow(((.5, .5), (1, 0)), n - 2)
    print(100 * pi, 100 * tau)