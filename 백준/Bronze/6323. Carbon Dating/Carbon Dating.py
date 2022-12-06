from math import*
i=1
while(S:=input())!='0 0': 
    w,d=map(int,S.split())
    y=int(log(810*w/d,2)*5730)
    print(f'Sample #{i}\nThe approximate age is {round(y,-3+(y<10000))} years.\n')
    i+=1