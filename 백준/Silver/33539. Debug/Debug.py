n=int(input())
print("yneos"[n<2 or any(n%i==0 for i in range(2,int(n**.5)+1))::2])