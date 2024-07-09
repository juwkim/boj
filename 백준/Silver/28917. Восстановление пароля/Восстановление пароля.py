n = len(s := [*input()])
l, r, k = map(int, input().split())
if abs(l - r) > n - 1 or (l and n == 1) or (r and n == 1):
    print("Impossible")
else:
    st = 0
    if l > r:
        st = n - 1
    s[st] = chr((ord(s[st]) - ord('a') + 26 - k % 26) % 26 + ord('a'))
    print(*s, sep="")
    print(st + 1)