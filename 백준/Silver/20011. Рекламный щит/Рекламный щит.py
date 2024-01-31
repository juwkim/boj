import sys
input = lambda: sys.stdin.readline().rstrip()

k, n, m = map(int, input().split())
board = [[input() for _ in range(n)] for _ in range(k)]
ans = set()
for x in range(n):
    for y in range(m):
        check = bytearray(k)
        for z in range(k):
            check[z] = board[z][x][y] == '*'
        ans.add(tuple(check))
print(len(ans))