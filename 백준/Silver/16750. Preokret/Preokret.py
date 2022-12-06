A = int(input())
numA = [(int(input()), 0) for _ in range(A)]
B = int(input())
numB = [(int(input()), 1) for _ in range(B)]

nums = sorted(numA + numB)

score = [0, 0]
res = []
prev = 0
for num, team in nums:
    score[team] += 1
    prev += num <= 1440
    if score[0] > score[1]:
        res.append(0)
    elif score[0] < score[1]:
        res.append(1)
print(prev)
ans = 0
for i in range(len(res)-1):
    if res[i] + res[i+1] == 1:
        ans += 1
print(ans)