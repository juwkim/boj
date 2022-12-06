import datetime as d
print('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()[d.date(2009,*map(int,input().split()[::-1])).weekday()])