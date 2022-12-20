ans = 1
top, btm, front, back, left, right = 1, 6, 2, 5, 4, 3
for _ in range(int(input())):
    cmd = input()
    if cmd == 'North':
        top, btm, front, back, left, right = front, back, btm, top, left, right
    elif cmd == 'South':
        top, btm, front, back, left, right = back, front, top, btm, left, right
    elif cmd == 'West':
        top, btm, front, back, left, right = right, left, front, back, top, btm
    elif cmd == 'East':
        top, btm, front, back, left, right = left, right, front, back, btm, top
    elif cmd == 'Right':
        top, btm, front, back, left, right = top, btm, right, left, front, back
    elif cmd == 'Left':
        top, btm, front, back, left, right = top, btm, left, right, back, front
    ans += top
print(ans)