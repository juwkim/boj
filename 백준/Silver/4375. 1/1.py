import sys
for n in sys.stdin:
    n,i=int(n),1
    while int('1'*i)%n:i+=1
    print(i)