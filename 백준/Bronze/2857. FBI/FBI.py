flag = 1
for i in range(1, 6):
    if 'FBI' in input():
        print(i)
        flag = 0
if flag:
    print('HE GOT AWAY!')