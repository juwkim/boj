import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    S, i = input(), 0
    while i < len(S) and S[i] not in "aeiou":
        i += 1
    if i == len(S):
        print(-1)
        continue
    ans, cnt = 1, 0
    for j in range(i + 1, len(S)):
        if S[j] in "aeiou":
            ans = ans * (cnt + 1) % 1000000007
            cnt = 0
        else:
            cnt += 1
    print(ans)