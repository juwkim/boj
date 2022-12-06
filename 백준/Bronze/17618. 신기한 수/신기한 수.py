count=0
for i in range(1,int(input())+1):
    count+=(i%sum(map(int,str(i)))==0)
print(count)