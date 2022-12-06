N,M,a,b,c,d=map(int,open(0).read().split())

if (a+b-c-d)//2:
    print('YNEOS'[N == 1 or M == 1 or (a+b-c-d)%2::2])
else:
    print('YNEOS'[(a+b-c-d)%2::2])