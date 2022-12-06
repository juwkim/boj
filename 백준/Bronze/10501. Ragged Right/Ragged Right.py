line = []
while True:
    try:
        line.append(len(input()))
    except:
        break
n = max(line)
print(sum((n-i)**2 for i in line[:-1]))