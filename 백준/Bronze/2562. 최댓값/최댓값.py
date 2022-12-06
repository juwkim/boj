Max, pos = 0, 0
for i in range(1, 10):
    num = int(input())
    if num > Max:
        Max = num
        pos = i

print(Max)
print(pos)