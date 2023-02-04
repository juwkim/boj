p = [num / 100 for num in map(int, input().split())]
prob = []
start = 0
for cnt in range(7, -1, -1):
    prob += [[0] * (8 - cnt) + p[start:start + cnt]]
    start += cnt

for i in range(1, 8):
    for j in range(i):
        prob[i][j] = 1 - prob[j][i]


round1 = []
for i in range(0, 8, 2):
    round1.append(prob[i][i+1])
    round1.append(prob[i+1][i])

round2 = []
for i in range(0, 8, 4):
    round2.append(round1[i] * (round1[i+2] * prob[i][i+2] + round1[i+3] * prob[i][i+3]))
    round2.append(round1[i+1] * (round1[i+2] * prob[i+1][i+2] + round1[i+3] * prob[i+1][i+3]))
    round2.append(round1[i+2] * (round1[i] * prob[i+2][i] + round1[i+1] * prob[i+2][i+1]))
    round2.append(round1[i+3] * (round1[i] * prob[i+3][i] + round1[i+1] * prob[i+3][i+1]))
    
for i in range(8):
    ans = 0
    if i <= 3:
        for j in range(4, 8):
            ans += round2[j] * prob[i][j]
    else:
        for j in range(4):
            ans += round2[j] * prob[i][j]
    ans *= round2[i]
    print(ans, end=' ')