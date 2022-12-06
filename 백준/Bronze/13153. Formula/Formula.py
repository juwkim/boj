x, y = zip(*[[*map(int, input().split())] for _ in range(3)])
a, b, c = [((x[i] - x[(i+1)%3])**2 + (y[i] - y[(i+1)%3])**2)**.5 for i in range(3)]
s = ((2*a*b)**2 - (a**2 + b**2 - c**2)**2)**.5 / 4
t = float(input()) * (a + b + c) / 2
print(100*(s-t)/t)