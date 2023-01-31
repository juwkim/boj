input()
A = [*map(int, input().split())]
input()
B = set(map(int, input().split()))
score = 0
for num in A:
    score += num
    if score in B:
        score = 0
print(score)