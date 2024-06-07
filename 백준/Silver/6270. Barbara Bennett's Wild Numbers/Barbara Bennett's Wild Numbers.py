import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(i, q):
	if i == n: return 0
	if W[i] == '?':
		return solve(i + 1, q - 1) + (9 - int(X[i])) * 10 ** (q - 1)
	if W[i] < X[i]: return 0
	if W[i] > X[i]: return 10 ** q
	return solve(i + 1, q)

while (W:=input()) != '#':
    n = len(X:=input())
    print(solve(0, W.count('?')))