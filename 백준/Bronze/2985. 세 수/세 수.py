k = input()
op, flag = '+-*/', 0
for i in range(4):
    t = k.replace(' ', op[i], 1).replace(' ', '==')
    if eval(t):
        flag = 1
        break
if not flag:
    for i in range(4):
        t = k.replace(' ', '==', 1).replace(' ', op[i])
        if eval(t):
            break
print(t.replace('==', '='))      