from math import *
while (n:= input()) != '0 0':
    x, y = map(float, n.split())
    time = ceil(pi*(x**2 + y**2)/100)
    print(f'The property will be flooded in hour {time}.')