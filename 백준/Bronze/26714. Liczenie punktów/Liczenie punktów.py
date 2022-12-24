N = int(input())
step = N // 10
cmp = 'T' * step
S = input()
print(sum(S[i:i + step] == cmp for i in range(0, len(S), step)))