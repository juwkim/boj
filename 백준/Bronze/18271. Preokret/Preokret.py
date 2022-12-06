score = [0, 0]
tie = 1

res = []
b_scored = 0
for i in range(int(input())):
    num = int(input()) - 1
    
    if num != b_scored:
        res.append(score.copy())
    b_scored = num
    
    score[num] += 1
    tie += (score[0] == score[1])

res.append(score)

flow = max([sum(j) - sum(i) for i, j in zip(res, res[1:]) if (i[0] - i[1]) * (j[0] - j[1]) < 0])

print(*score)
print(tie)
print(flow)