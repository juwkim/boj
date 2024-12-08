S, ans = input(), "abcdefghijklmnopqrstuvwxzy"
if len(S) < 26:
    ans = S + min(set("abcdefghijklmnopqrstuvwxyz") - set(S))
elif S == "zyxwvutsrqponmlkjihgfedcba":
    ans = -1
else:
    for i in range(24, 0, -1):
        p = set(range(ord(S[i]) + 1, ord('z') + 1)) - set(map(ord, S[:i]))
        if p:
            ans = S[:i] + chr(min(p))
            break
print(ans)