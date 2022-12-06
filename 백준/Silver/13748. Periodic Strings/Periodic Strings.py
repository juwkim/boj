s = input()
l = len(s)
for i in range(1, l+1):
    if l % i == 0:
        msg = s[:i]

        flag = True
        for j in range(i, l, i):
            tmp = s[j:j+i]
            if tmp != msg[-1] + msg[:-1]:
                flag = False
                break
            msg = tmp
        if flag:
            print(i)
            break