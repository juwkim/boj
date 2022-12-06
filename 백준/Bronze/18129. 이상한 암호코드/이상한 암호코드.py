S, K = input().split()
S, K = S.lower(), int(K)
a, cnt = S[0], 1
check = set()
for i in range(1, len(S)):
    if S[i] == a:
        cnt += 1
    else:
        if a not in check:
            check.add(a)
            print(+(cnt>=K), end='')
        a = S[i]
        cnt = 1
if a not in check:
    print(+(cnt>=K), end='')