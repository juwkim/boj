A,B,C,X,Y=map(int,input().split())
print(min(2*C*max(X,Y),A*X+B*Y,2*C*min(X,Y)+abs(X-Y)*[A,B][X<Y]))