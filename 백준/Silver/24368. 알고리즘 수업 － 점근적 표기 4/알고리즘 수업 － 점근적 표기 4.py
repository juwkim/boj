g = lambda: [*map(int, input().split())]

x, y, z = g()
c = int(input())
n = int(input())
p=c-x
if p:    
    print((p>0)*((y*y<=-4*z*p)or((y<=2*n*p)*(p*n-y>=z/n))))
elif y:
    print((y < 0) * (y * n + z <= 0))
else:
    print(+(z <= 0))