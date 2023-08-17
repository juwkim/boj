level, stat = 0, 0
team = sorted(int(input()) for _ in range(int(input())))[-42:]
for l in team:
    level += l
    if l < 60:
        pass
    elif l < 100:
        stat += 1
    elif l < 140:
        stat += 2
    elif l < 200:
        stat += 3
    elif l < 250:
        stat += 4
    else:
        stat += 5
print(level, stat)