N = int(input())
S = input()
idx = N - 1
while idx >= 1 and S[idx] == '0':
    idx -= 1
if idx == 0:
    print(0)
else:
    print(1 + S[:idx].count('0'))