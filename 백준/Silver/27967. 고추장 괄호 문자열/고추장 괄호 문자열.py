N = int(input())
S = input()
print(S.replace('G', '(', N // 2 - S.count('(')).replace('G', ')'))