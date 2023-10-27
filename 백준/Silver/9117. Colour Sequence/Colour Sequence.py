import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    i = 0
    ans = "lose"
    for a, b in zip(input(), input()):
        if a == '*' or b == '*' or a == s[i] or b == s[i]:
            i += 1
            if i == len(s):
                ans = "win"
                break
    print(ans)