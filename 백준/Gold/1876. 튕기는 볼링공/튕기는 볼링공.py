from math import*
exec("T,X=input().split();T=float(T)%(o:=.85/tan(X:=radians(int(X))));print('yneos'[abs(T*sin(X)-.85*(2*T>o)*cos(X))>.16::2]);"*int(input()))