g=lambda:[*map(int, input().split())]
k=g()
h=lambda:sum(x*y for x,y in zip(k,g()))
print(max([h()+h()+h()for _ in range(int(input()))]))