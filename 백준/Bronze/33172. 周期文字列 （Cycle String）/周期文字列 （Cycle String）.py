N = int(input())
S = input()
ans = "No"
for l in range(1, len(S) // 2 + 1):
    if len(S) % l:
        continue
    p = S[:l]
    if all(S[i * l:i * l + l] == p for i in range(1, len(S) // l)):
        ans = "Yes"
        break
print(ans)