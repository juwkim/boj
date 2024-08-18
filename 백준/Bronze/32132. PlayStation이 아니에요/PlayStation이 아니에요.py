N = int(input())
S = input()
i = 0
while i < len(S) - 2:
    if S[i] == 'P' and S[i + 1] == 'S' and S[i + 2] in "45":
        S = S[:i + 2] + S[i + 3:]
    else:
        i += 1
print(S)