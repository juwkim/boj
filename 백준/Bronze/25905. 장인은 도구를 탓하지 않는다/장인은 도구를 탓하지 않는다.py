from math import factorial
_, *l = sorted(float(input()) * 10 for _ in range(10))
ans = 1
for num in l:
    ans *= num
print(ans / factorial(9))