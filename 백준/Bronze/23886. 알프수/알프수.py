s = input()
a = [int(j) - int(i) for i, j in zip(s, s[1:])]

if a[0] > 0 and a[-1] < 0:
    cur = a[0]
    flag = True
    for i in range(1, len(a)):
        if a[i] == 0:
            flag = False
            break
        elif cur * a[i] > 0:
            if cur != a[i]:
                flag = False
                break
        else:
            cur = a[i]
    print('ALPSOO' if flag else 'NON ALPSOO')    
else:
    print('NON ALPSOO')