c=1
while T:=int(input()):
 a=0;
 for i in range(1,T//3):a+=(T-3*i-1)//2
 print(f'Case #{c}: {T}:{a}')
 c+=1