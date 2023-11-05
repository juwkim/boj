import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
buf = [input() for _ in range(N)]
ans = []
i = 0
while i < N:
    if buf[i] != "Present!" and (i == N - 1 or buf[i + 1] != "Present!"):
        ans.append(buf[i])
    i += 1
if ans:
    print(*ans, sep="\n")
else:
    print("No Absences")