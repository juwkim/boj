import sys
input = lambda: sys.stdin.readline().rstrip()
from datetime import datetime

def solve(s):
    if s.count('/') != 1:
        return "invalid"
    left, right = s.split('/')
    if len(left) != 6 or len(right) <= 2 or len(right) >= 5:
        return "invalid"
    yy, mm, dd = int(left[0:2]), int(left[2:4]), int(left[4:6])
    if 1 <= mm <= 12:
        gender = "boy"
    elif 51 <= mm <= 62:
        mm -= 50
        gender = "girl"
    else:
        return "invalid"
    year = 1900 + yy if yy >= 20 else 2000 + yy
    try:
        birthdate = datetime(year, mm, dd)
    except ValueError:
        return "invalid"
    if not (datetime(1920, 1, 1) <= birthdate <= datetime(2009, 12, 31)):
        return "invalid"
    if year >= 1954:
        if len(right) != 4 or int(left + right) % 11:
            return "invalid"
    elif len(right) != 3:
        return "invalid"
    return gender

while (line:=input())[0] != 'e':
    print(solve(line))