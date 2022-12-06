input()
room = input().split()
x1, d1 = input().split()
x2, d2 = input().split()
*room, x1, x2 = map(int, room + [x1, x2])

if d1 == 'right':
    num_student = sum(room[x1-1:])
else:
    num_student = sum(room[:x1])

if d2 == 'right':
    num_empty = room[x2-1:].count(0)
else:
    num_empty = room[:x2].count(0)
print(num_student, num_empty)