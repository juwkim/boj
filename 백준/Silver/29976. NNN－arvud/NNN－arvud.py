alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())
if N in (2, 3, 6):
    print("EI OLE")
else:
    if N == 4:
        sols_f = [[1,2,1,0],[2,0,2,0]]
    elif N == 5:
        sols_f = [[2,1,2,0,0]]
    else:
        f = [0] * N
        f[0], f[1], f[2], f[N - 4] = N - 4, 2, 1, 1
        sols_f = [f]
    ans = sorted("".join([alpha[f[0]]] + [alpha[f[N-i]] for i in range(1, N)]) for f in sols_f)
    print(*ans, sep="\n")