import datetime
dt = '21/03/2012'
month, day = map(int, input().split())    
ans = datetime.date(2007, month, day)
print(ans.strftime("%A")[:3].upper())