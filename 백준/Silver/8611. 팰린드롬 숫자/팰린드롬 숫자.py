N = int(input())
flag = False
for base in range(2, 11):
    tmp = N
    num = ''
    while True:
        tmp, q = divmod(tmp, base)
        num = str(q) + num
        if tmp == 0:
            break
    if num == num[::-1]:
        print(base, num)
        flag = True
if not flag:
    print('NIE')