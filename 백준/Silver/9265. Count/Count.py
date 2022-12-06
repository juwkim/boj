from bisect import*
from collections import*
def r():
 a,b,c,d=f.read(4)
 return(d<<24)+(c<<16)+(b<<8)+a
f,d=open(0,"rb"),defaultdict(int)
for i in range(r()*r()):d[r()]+=1
n=sorted(d.keys())
while True:
 try:print(sum(d[s]for s in n[bisect_left(n,r()):bisect_right(n,r())]))
 except:break