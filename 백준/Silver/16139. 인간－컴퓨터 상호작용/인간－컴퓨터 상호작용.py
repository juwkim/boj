S = input()
px = [[0] * (len(S) + 1) for _ in range(26)]
for i in range(1, 1 + len(S)):
    for j in range(26):
        px[j][i] = px[j][i-1]
    px[ord(S[i-1]) - 97][i] += 1

for _ in range(int(input())):
    a, *buf = input().split()
    l, r = map(int, buf)
    ans = px[ord(a) - 97][r+1] - px[ord(a) - 97][l] 
    print(ans)