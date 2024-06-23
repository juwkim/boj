import math
a=[0,3]
for i in range(2,1001):a.append(a[i-1]+2*sum(1==math.gcd(i,j)for j in range(1,i)))
for l in[*open(0)][1:]:print(a[int(l)])