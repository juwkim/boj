import sys
input = sys.stdin.readline

N, R = map(int, input().split())
dic = {}
for _ in range(N):
    name, *l = input().split()
    B, size, D, *nums = map(int, l)
    L, U = nums[::2], nums[1::2]
    C = [0] * (D - 1) + [size]
    for d in range(D - 2, -1, -1):
        C[d] = C[d + 1] * (U[d + 1] - L[d + 1] + 1)
    C0 = B - sum(C[d] * L[d] for d in range(D))
    dic[name] = D, L, U, C, C0

for _ in range(R):
    name, *idx = input().split()
    D, L, U, C, C0 = dic[name]
    inside = ", ".join(idx)
    addr = C0 + sum(int(idx[d]) * C[d] for d in range(D))
    print(f"{name}[{inside}] = {addr}")