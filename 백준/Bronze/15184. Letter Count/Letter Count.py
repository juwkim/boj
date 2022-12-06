from collections import*
a=Counter(input().upper())
for i in range(65,91):
    print(f'{chr(i)} | {"*"*a[chr(i)]}')