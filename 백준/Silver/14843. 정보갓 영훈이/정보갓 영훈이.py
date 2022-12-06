score = 0
for _ in range(int(input())):
    S, *l = input().split()
    A, T, M = map(int, l)
    S = float(S)
    
    score += S * (A + 1) * (T + M) / (A * T)
score /= 4

P = int(input())
nums = [float(input()) for _ in range(P)]

if 1 + sum(score < num for num in nums) <= 0.15 * (P + 1):
    print(f'The total score of Younghoon "The God" is {score:.2f}.')
else:
    print(f'The total score of Younghoon is {score:.2f}.')