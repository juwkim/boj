import sys
input = sys.stdin.readline

l, r = -10**18, 10**18
ans = "Hmm..."
for i in range(1, 1 + int(input())):
    num, cmd = input().split()
    num = int(num)
    if cmd == '^':
        l = max(l, num + 1)
    else:
        r = min(r, num - 1)
    if ans == "Hmm..." and l == r:
        ans = f"I got it!\n{i}"
    elif l > r:
        ans = f"Paradox!\n{i}"
        break
print(ans)