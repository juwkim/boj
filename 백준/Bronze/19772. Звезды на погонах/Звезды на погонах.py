a, b, c, d, e = map(int, input().split())
num = min(b, c - 1)
Min = d + num - a - e
Max = Min + max(0, e - d - 1) + b - num
print(Min, Max)