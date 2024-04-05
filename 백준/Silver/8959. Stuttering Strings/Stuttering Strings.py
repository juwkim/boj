import sys

def solve(star, bang):
    if len(cur) == n:
        ans.append(''.join(cur))
        return
    if star + 1 <= nstar:
        cur.append('*')
        solve(star + 1, 0)
        cur.pop()
    if bang + 1 <= nbang:
        cur.append('!')
        solve(0, bang + 1)
        cur.pop()

tc = 1
while True:
    n, nstar, nbang = map(int, sys.stdin.readline().split())
    if n == nstar == nbang == 0:
        break
    print(f"Sequence set {tc}")
    tc += 1
    ans, cur = [], []
    solve(0, 0)
    for l in sorted(ans, reverse=True):
        print(l)