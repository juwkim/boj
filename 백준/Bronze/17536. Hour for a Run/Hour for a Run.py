import math
t=eval(input().replace(' ','*'))
print(*[math.ceil(t*i/10)for i in range(1, 10)])