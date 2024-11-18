import sys
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())
score = int(input().split()[1])
l = []
for _ in range(N - 1):
    a, b = input().split()
    if a[2:4] == "24":
        b = int(b)
        l.append(b + max(0, Y - X + b))
l.sort()
if len(l) + 1 <= M:
    print("YES")
    print(0)
else:
    todo = l[-M] - score
    if todo > Y:
        print("NO")
    else:
        print("YES")
        print(max(0, todo))