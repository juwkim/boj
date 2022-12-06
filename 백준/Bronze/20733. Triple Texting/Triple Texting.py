d=len(a:=input())//3
print(sorted(a[i:i+d]for i in range(0,d*3,d))[1])