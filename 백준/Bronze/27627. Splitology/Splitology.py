ans = 'NO'
S = input()
for i in range(1, len(S)):
    a, b = S[:i], S[i:]
    if a == a[::-1] and b == b[::-1]:
        ans = f'{a} {b}'
        break
print(ans)