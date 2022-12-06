Q, Axis = [0, 0, 0, 0], 0 
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        Q[0] += 1
    elif x > 0 and y < 0:
        Q[3] += 1
    elif x < 0 and y > 0:
        Q[1] += 1
    elif x < 0 and y < 0:
        Q[2] += 1
    else:
        Axis += 1
for i in range(4):
    print(f'Q{i+1}: {Q[i]}')
print(f'AXIS: {Axis}')