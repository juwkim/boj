a, m = map(int, input().split())
t = 1
while True:
    k = (1 + m*t)/a
    if k == int(k):
        break
    t += 1
print(int(k))