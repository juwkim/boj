N = int(input())
total_score = 0
total_credit = 0

for _ in range(N):
    s = input().split()
    credit = int(s[1])
    
    score = max(0, 69 - ord(s[2][0]))
    if score:
        score += 0.3 * ('-0+'.index(s[2][1]) - 1)
    
    total_credit += credit
    total_score += credit * score

print(f'{total_score/total_credit + 10**(-10):#.2f}')