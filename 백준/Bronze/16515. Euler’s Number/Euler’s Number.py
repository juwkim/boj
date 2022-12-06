total, s = 1, 1
for i in range(1, int(input())+1):
    s *= i
    total += 1/s
print(total)