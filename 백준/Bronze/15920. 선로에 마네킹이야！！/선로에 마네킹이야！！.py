N = int(input())
S = [i for i, c in enumerate(input()) if c == 'W']
if len(S) < 2:
    print(0)
elif S[1] - S[0] > 1:
    print(6)
else:
    print(5 - S[0] % 2 * 4)