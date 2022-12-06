score = [0]
for _ in range(10):
    score.append(score[-1] + int(input()))
print(min(score, key=lambda x: (abs(100 - x), 100 - x)))