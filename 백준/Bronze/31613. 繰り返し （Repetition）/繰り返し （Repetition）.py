X,N=map(int,open(0))
a=0
while X<N:X=(X+1,X*2,X*3)[X%3];a+=1
print(a)