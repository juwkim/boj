p=sorted(eval("input().split(),"*int(input())),key=lambda x:[*map(int,x[:0:-1])])
print(p[-1][0],p[0][0])