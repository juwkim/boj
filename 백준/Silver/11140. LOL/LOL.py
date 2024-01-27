import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    s = input()
    if "lol" in s:
        ans = 0
    elif any(word in s for word in ("lo", "ol", "ll")) or any(s[i] == "l" and s[i + 2] == "l" for i in range(len(s) - 2)):
        ans = 1
    elif any(word in s for word in ("l", "o")):
        ans = 2
    else:
        ans = 3
    print(ans)