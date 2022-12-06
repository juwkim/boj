I,g=input,lambda:sorted(map(int,I().split()))
for i in range(int(I())):I();print(f'Case #{i+1}: {sum(x*y for x,y in zip(g(),g()[::-1]))}')