input()
total, plus = 0, 0
for num in map(int, input().split()):
    if num:
        plus += 1
        total += plus
    else:
        plus = 0
print(total)