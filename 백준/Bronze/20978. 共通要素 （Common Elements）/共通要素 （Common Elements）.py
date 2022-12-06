I=lambda:{*input().split()}
I()
print(*sorted(I()&I(),key=int))