cnt = 0
flag = 1
for num in input():
    if flag:
        num = sum(divmod(int(num) * 2, 10))
    cnt += int(num)
    flag ^= 1
print('NE' if cnt % 10 else 'DA')