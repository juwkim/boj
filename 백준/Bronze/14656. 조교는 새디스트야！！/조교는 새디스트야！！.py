N = int(input())
student = [*map(int, input().split())]
sorted_student = sorted(student)
seat = [student[i] != sorted_student[i] for i in range(N)]
print(seat.count(True))