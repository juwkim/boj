num = int(input())
flag = 0
for i in range(1, int(num**.5)+1):
    k = (num - i**2)**.5
    if k == int(k):
        k = int(k)
        flag = 1
        break
if flag:
    print(f'{0} {0}\n{i} {k}\n{-k} {i}\n{i-k} {i+k}')
else:
    print('Impossible')