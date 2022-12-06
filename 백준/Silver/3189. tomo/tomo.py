A,B,C=map(int,input().split())
a,i=[S:=(A*B%(t:=10**(len(str(C)))))],1
while S!=C and S not in a[:-1]:a+=[S:=S*B%t];i+=1
print('NIKAD'if S-C else i)