a=[input().split()for _ in range(10)]
print(+any(1==len({*x})for x in a+[*zip(*a)]))