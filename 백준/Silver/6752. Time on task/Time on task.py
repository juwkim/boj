T = int(input())
chores = sorted(int(input()) for _ in range(int(input())))
for i in range(len(chores)):
    T -= chores[i]
    if T < 0:
        print(i)
        break