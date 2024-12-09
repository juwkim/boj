def f(s):
 h,m=map(int,s.split(':'))
 d=h%12*60-m*11
 return min(d%720,-d%720),s
for l in[*open(0)][1:]:print(sorted(l.split(),key=f)[2])