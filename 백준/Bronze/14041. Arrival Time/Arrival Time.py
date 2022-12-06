h,m=map(int,input().split(':'))
t=h*60+m
print('%02d:%02d'%divmod((max(min(t-180,420-t//2,210),min(t-660,690-t//2),120)+t)%1440,60))