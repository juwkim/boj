students = []
for _ in range(int(input()) + 1):
    t, who = input().split()
    if who[0] == 't':
        teacher_time = t
    else:
        students.append(t)
time = input()
print(sum(s >= max(time, teacher_time) for s in students))