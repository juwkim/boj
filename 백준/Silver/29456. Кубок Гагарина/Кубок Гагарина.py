p1_h, p2_a = map(float, input().split())
p1_a, p2_h = map(float, input().split())
prob = [(p1_h, p2_a), (p1_h, p2_a), (p1_a, p2_h), (p1_a, p2_h), (p1_h, p2_a), (p1_a, p2_h), (p1_h, p2_a)]
s, t = map(int, input().split('-'))
if s == 4:
    winner = 0
    s -= 1
else:
    winner = 1
    t -= 1
ans = 0
def solve(i, p1, p2, num):
    if (p1, p2) == (s, t):
        return num * prob[i][winner]
    if p1 > s or p2 > t:
        return 0
    return solve(i + 1, p1 + 1, p2, num * prob[i][0]) + solve(i + 1, p1, p2 + 1, num * prob[i][1])
print(solve(0, 0, 0, 1))