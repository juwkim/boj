g=lambda a:len(a)==2 and''.join(map(str,a))or g([sum(x)%10 for x in zip(a,a[1:])])
a=[0]*16
for i,x in enumerate(zip(input(),input())):a[2*i],a[2*i+1]=map(int,x)
print(g(a))