t = 1
n = int(input())
while n >= (2*t**3 + t)//3:
    t += 1
print(t-1)