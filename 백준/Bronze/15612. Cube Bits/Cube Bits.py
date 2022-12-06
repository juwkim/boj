for n in[*map(int,open(0))][1:]:
 s=''
 while n:s=str(n%3)+s;n//=3
 print(s or 0)