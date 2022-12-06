from math import*
exec("T,X=input().split();T=float(T)%(o:=0.85/tan(X:=radians(int(X))));print('yneos'[abs(T*sin(X)-0.85*(2*T>o)*cos(X))>0.16::2]);"*int(input()))