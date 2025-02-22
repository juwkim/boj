B = int(input())
D = {k: v for v, k in enumerate(input().split())}
s, i = input(), 0
ans = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[i:j] not in D:
        j += 1
    ans = ans * B + int(D[s[i:j]])
    i = j
print(ans)