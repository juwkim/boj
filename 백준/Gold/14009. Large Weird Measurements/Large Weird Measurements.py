N, *S = map(int, open(0).read().split())
i, ans, flag = 0, N, 0
while i < N - 1:
    k = i
    if S[i] < S[i+1]:
        flag = 1
    elif S[i] > S[i+1]:
        flag = 2
    i += 1
    
    while flag and i < N - 1:
        if flag == 1:
            if S[i] > S[i+1]:
                flag += 1
                i += 1
            else:
                flag = 0
                ans += (i - k) * (i - k + 1) // 2
                if S[i] == S[i+1]:
                    i += 1
        else:
            if S[i] < S[i+1]:
                flag -= 1
                i += 1
            else:
                flag = 0
                ans += (i - k) * (i - k + 1) // 2
                if S[i] == S[i+1]:
                    i += 1
ans += (i - k) * (i - k + 1) // 2
print(ans)