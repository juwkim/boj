Octopus = '-\(@?>&%'
while True:
    num = input()
    if num == '#':
        break
    for i in range(0, 8):
        num = num.replace(Octopus[i], str(i))
    num = list(reversed([int(i.replace('/', '-1')) for i in num]))
    total = sum([num[i] * 8**i for i in range(len(num))])
    print(total)