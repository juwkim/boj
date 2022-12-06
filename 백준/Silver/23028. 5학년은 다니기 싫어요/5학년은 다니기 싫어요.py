g=lambda:map(int,input().split())
N,A,B=g()
exec('X,Y=g();b=min(Y,6-(a:=min(X, 6)));A+=3*a;B+=3*(a+b);'*(8-N))
print(['Nae ga wae','Nice'][(A>67)*(B>131)])