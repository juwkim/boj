import datetime as dt
while(s:=input())[0]!='0':
    try:
        d, m = s.split()
        datetime_object = dt.datetime.strptime(m, "%B")
        m = datetime_object.month
        a = dt.datetime.strptime(f"2007 {d} {m}", "%Y %d %m")
        b = dt.datetime(2007, 8, 4)
        print(['Happy birthday', 'Yes', 'No'][(a < b) - (b < a)])
    except:
        print('Unlucky')