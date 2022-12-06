A,B=input().split()
print(min(sum(a!=b for a,b in zip(A,B[i:]))for i in range(len(B)-len(A)+1)))