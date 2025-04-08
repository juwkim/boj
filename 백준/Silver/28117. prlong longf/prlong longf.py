l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
N = int(input())
S = input()
ans = 1
i, cnt = 0, 0
while i < N:
    if S[i:i+4] == "long":
        cnt += 1
        i += 4
    else:
        ans *= l[cnt]
        cnt = 0
        i += 1
if cnt:
    ans *= l[cnt]
print(ans)