g=lambda:sorted(map(int,input().split()))
g()
print('DNAE'[any(x>y for x,y in zip(g(),g()))::2])