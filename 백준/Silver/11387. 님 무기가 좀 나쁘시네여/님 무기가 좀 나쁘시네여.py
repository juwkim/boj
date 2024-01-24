import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve(l):
    a, b, c, d, e = l
    return a * (100 + b) * (max(0, 100 * (100 - c)) + min(100, c) * d) * (100 + e)

cri = g(); si = solve(cri)
pabu = g(); ti = solve(pabu)
for i, (A, B) in enumerate(zip(g(), g())):
    cri[i] += B - A
    pabu[i] += A - B
sj = solve(cri)
tj = solve(pabu)
print("0-+"[(si > sj) - (si < sj)])
print("0-+"[(ti > tj) - (ti < tj)])