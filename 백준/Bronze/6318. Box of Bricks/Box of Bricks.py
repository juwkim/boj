i=1
while n:=int(input()):
    s=[*map(int,input().split())]
    m=sum(s)//n
    print(f'Set #{i}\nThe minimum number of moves is {sum(abs(i-m)for i in s)//2}.\n')
    i+=1