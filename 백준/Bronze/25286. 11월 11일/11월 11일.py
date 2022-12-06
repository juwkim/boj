import datetime as d
exec('y,m=map(int,input().split());a=d.datetime(y,m,m)-d.timedelta(m);print(a.year,a.month,a.day);'*int(input()))