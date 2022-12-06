n,f,i=sum(ord(i)-38-58*('`'<i<'{')for i in input()),0,5
if n<4:f=0
elif n%2==0 or n%3==0:f=1
else:
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:f=1;break
        i+=6
print('It is'+' not'*f+' a prime word.')