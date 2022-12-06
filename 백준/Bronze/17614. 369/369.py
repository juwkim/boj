a=0
for i in range(1,int(input())+1):
    i=str(i)
    a+=sum([i.count('3'),i.count('6'),i.count('9')])
print(a)