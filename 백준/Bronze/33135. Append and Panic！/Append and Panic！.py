S = input()
for i in range(1, len(S)):
    if "".join(sorted({*S[:i]})) == S[i:]:
        print(i)
        break