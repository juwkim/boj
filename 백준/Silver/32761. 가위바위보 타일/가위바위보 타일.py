N,S=open(0)
l=[0]*3
for i in range(3):
 for c in S:l[i]+="SPR"[(i+l[i])%3]==c
print(int(N)-max(l)//3*3)