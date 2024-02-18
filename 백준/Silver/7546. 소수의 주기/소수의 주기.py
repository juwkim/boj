import sys
input = sys.stdin.readline
for tc in range(1, 1 + int(input())):
    b, x, y = input().split()
    x, y = int(x, b:=int(b)), int(y, b)
    check = [0] * y
    ans, i = 0, 0
    while (x := x * b % y) and check[x] == 0:
        check[x] = i
        i += 1
    print(f"Scenario #{tc}:\n{i - check[x]}\n")