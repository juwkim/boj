K, L = map(int, input().split())
flag = 1
for i in range(2, L):
    if K % i == 0:
        flag = 0
        break
print('GOOD' if flag else f'BAD {i}')