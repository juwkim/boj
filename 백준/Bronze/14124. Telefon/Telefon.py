def to_base(num, base):
    res = ''
    while True:
        num, q = divmod(num, base)
        res = str(q) + res
        if num == 0:
            break
    return res

num = input()
ans = 10
cnt = sum(i != j for i, j in zip(num, num[1:]))

i_num = int(num)
for i in range(9, 1, -1):
    to_i = to_base(i_num, i)
    tmp = sum(i != j for i, j in zip(to_i, to_i[1:]))
    if tmp < cnt:
        ans = i
        cnt = tmp
print(ans)