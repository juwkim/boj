import sys
for n in sys.stdin:
    a,n,k={*map(str,range(10))},int(n),0
    while a:k+=1;a-={i for i in str(n*k)}
    print(k)