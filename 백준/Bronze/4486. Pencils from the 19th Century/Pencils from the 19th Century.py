from math import*
P,R,i=print,range,1
while n:=int(input()):
    P(f'Case {i}:\n{n} pencils for {n} cents')
    a=[]
    for x in R(1,ceil(n/4)):
        for y in R(1,2*n-8*x):
            if 15*x+y==3*n:a+=[[x,y,n-x-y]]
    if a:
        for x,y,z in a:P(f'{x} at four cents each\n{y} at two for a penny\n{z} at four for a penny\n')
    else:P('No solution found.\n')
    i+=1