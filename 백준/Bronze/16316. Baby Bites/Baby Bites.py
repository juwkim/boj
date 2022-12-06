n = int(input())
baby = input().split()
flag = 1
for i in range(n):
    if baby[i] != 'mumble' and baby[i] != str(i+1):
        flag = 0
        break
print('makes sense' if flag else 'something is fishy')