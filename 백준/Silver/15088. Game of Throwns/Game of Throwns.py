g = lambda: [*map(int, input().split())]

n, k = g()
cmds = input().split()
while True:
    try:
        idx = cmds.index('undo')
        amount = cmds[idx+1]
        del cmds[idx-int(amount):idx+2]
    except:
        break
print(sum(map(int, cmds)) % n)