import sys
input = sys.stdin.readline
for tc in range(1, 1 + int(input())):
    b, x, y = input().split()
    x, y = int(x, b:=int(b)), int(y, b)
    check = [0] * y
    ans, i = 0, 0
    while x := x * b % y:
        if check[x]:
            ans = i - check[x]
            break
        check[x] = i
        i += 1
    print(f"Scenario #{tc}:\n{i - check[x]}\n")