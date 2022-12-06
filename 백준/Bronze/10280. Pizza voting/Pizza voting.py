n,p=map(int,input().split())
print('YNEOS'[not(n//3<p<=n-n//3-(n%3==2))::2])