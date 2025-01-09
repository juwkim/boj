L, S = input().split()
L = int(L)
ans, l = 0, 0
for r in range(L):
    if S[r] == 'B':
        if S[l] != 'B':
            l = r
    elif S[l] == 'B':
        if l - 1 >= 0 and S[l - 1] == '.' and S[r] == 'W':
            idx = l - 2
            while True:
                if idx < 0 or S[idx] == '.':
                    ans = max(ans, r - l)
                    break
                if S[idx] == 'B':
                    break
                idx -= 1
        elif l - 1 >= 0 and S[l - 1] == 'W' and S[r] == '.':
            idx = r + 1
            while True:
                if idx == L or S[idx] == '.':
                    ans = max(ans, r - l)
                    break
                if S[idx] == 'B':
                    break
                idx += 1
        l = r
print(ans)