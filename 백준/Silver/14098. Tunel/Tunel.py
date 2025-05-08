import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
in_order = {input(): i for i in range(N)}
outs = [input() for _ in range(N)]
out_order = {car: i for i, car in enumerate(outs)}

ans = 0
for i, car in enumerate(outs):
    ans += any(in_order[car] > in_order[other] for other in outs[i+1:])
print(ans)