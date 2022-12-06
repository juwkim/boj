while (s:= input()) != '#':
    flag = True
    while (e:= input()) != '#':
        if flag and len(s) == len(e) and sum(i != j for i, j in zip(s, e)) == 1:
            s = e
        else:
            flag = False
    print('Correct' if flag else 'Incorrect')