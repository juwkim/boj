buf = sorted((int(l[1]), l[0]) for l in map(str.split, open(0)))
tall, name = zip(*buf)
i = 0
while i < len(buf) - 1:
    if tall[i+1] - tall[i] <= 2:
        print(name[i], name[i+1])
        i += 2
    else:
        i += 1