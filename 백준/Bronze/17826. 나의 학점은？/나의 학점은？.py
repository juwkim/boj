a=input().split().index(input())
if a<5:t='A+'
elif a<15:t='A0'
elif a<30:t='B+'
elif a<35:t='B0'
elif a<45:t='C+'
elif a<48:t='C0'
else:t='F'
print(t)