g = lambda: [*map(int, input().split())]


def solve():
    a, b = 0, 0
    d = 0
    for i in range(n):
        op = ops[i]
        if op == 'Forward':
            if d == 0:
                b += 1
            elif d == 1:
                a += 1
            elif d == 2:
                b -= 1
            else:
                a -= 1
        elif op == 'Left':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
    return a, b
        
x, y = g()
n = int(input())
ops = [input() for _ in range(n)]
for i in range(n):
    tmp = ops[i]
    cmds = ['Forward', 'Right', 'Left']
    cmds.remove(ops[i])
    
    ops[i] = cmds[0]
    a, b = solve()
    if a == x and b == y:
        print(i+1, cmds[0])
        break
    
    ops[i] = cmds[1]

    a, b = solve()
    if a == x and b == y:
        print(i+1, cmds[1])
        break
    
    ops[i] = tmp