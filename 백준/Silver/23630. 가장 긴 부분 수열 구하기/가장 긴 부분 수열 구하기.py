N = int(input())
l = [0] * 20
for A in map(int, input().split()):
    i = 0
    while A:
        l[i] += A & 1
        A >>= 1
        i += 1
print(max(l))