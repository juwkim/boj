import sys
input = lambda: sys.stdin.readline().rstrip()

l = ["" for _ in range(50000)]
for _ in range(int(input())):
    name = input()
    a, b = input().split()
    x1, y1 = map(int, a.split("."))
    x2, y2 = map(int, b.split("."))
    s = x1 * 10 + y1
    e = x2 * 10 + y2
    for i in range(s, e + 1):
        l[i] = name
for _ in range(int(input())):
    y = int(input())
    ans = []
    for i in range(y * 10, y * 10 + 10):
        if not l[i]:
            continue
        if not ans or ans[-1] != l[i]:
            ans.append(l[i])
    print(f"Galactic year {y}:", end=' ')
    if ans:
        print(*ans, sep=", ")
    else:
        print("None")