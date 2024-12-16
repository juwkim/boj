import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    S = int(input())
    for _ in range(S): input()
    ans, check = 0, set()
    for _ in range(int(input())):
        l = input()
        check.add(l)
        if len(check) == S:
            ans += 1
            check = {l}
    print(f"Case #{tc}: {ans}")