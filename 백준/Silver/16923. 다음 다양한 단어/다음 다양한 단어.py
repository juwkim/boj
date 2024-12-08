S = input()
if len(S) < 26:
    t = min(set("abcdefghijklmnopqrstuvwxyz") - set(S))
    print(S + t)
elif S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
else:
    i = 24
    ans = "abcdefghijklmnopqrstuvwxzy"
    while i > 0:
        p = set(range(ord(S[i]) + 1, ord('z') + 1)) - set(map(ord, S[:i]))
        if p:
            ans = S[:i] + chr(min(p))
            break
        i -= 1
    print(ans)