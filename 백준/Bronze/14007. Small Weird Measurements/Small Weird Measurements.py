N = int(input())
S = [*map(int, input().split())]
check, ans = [*range(N-1)], N

for i in range(N-1):
    if S[i] != S[i+1]:
        ans += 1
        check[i] += 1
    else:
        check[i] = 0

check = [i for i in check if 0 < i < N - 1]

while check:
    for index, value in enumerate(check):
        if S[value-1] > S[value] < S[value+1]:
            ans += 1
            check[index] += 1
        elif S[value-1] < S[value] > S[value+1]:
            ans += 1
            check[index] += 1
        else:
            check[index] = 0
    check = [i for i in check if 0 < i < N - 1]
print(ans)