g=lambda:map(int,input().split(':'))
h1,m1,s1=g()
h2,m2,s2=g()
t=((h2-h1)*3600+(m2-m1)*60+s2-s1-1)%86400+1
print(f'{t//3600:#02d}:{t%3600//60:#02d}:{t%3600%60:#02d}')