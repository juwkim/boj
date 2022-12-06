h, M = map(int, [input(), input()])
t = 1

while t <= M and -6 * t**4 + h * t**3 + 2 * t**2 + t > 0:
    t += 1

if t > M:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour:", t)