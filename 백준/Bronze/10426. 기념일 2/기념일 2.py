import datetime as d
a, b = input().split()
aniversary = d.datetime.strptime(a, '%Y-%m-%d') + d.timedelta(int(b) - 1)
print(aniversary.strftime('%Y-%m-%d'))