from datetime import datetime

s = input()
year = int(s.split()[2])
dt = datetime.strptime(s, "%B %d, %Y %H:%M")
print(100 * (dt - datetime(year, 1, 1)).total_seconds() / (datetime(year + 1, 1, 1) - datetime(year, 1, 1)).total_seconds())