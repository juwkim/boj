from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    buf = []
    for c in input():
        if c == '-':
            continue
        elif c.isdigit():
            buf.append(c)
        else:
            buf.append(str((ord(c) - 59 - (c > 'Q')) // 3))
    buf.insert(3, '-')
    dic[''.join(buf)] += 1

cnt = 0
for k, v in sorted(dic.items()):
    if v > 1:
        print(k, v)
        cnt += 1
if cnt == 0:
    print('No duplicates.')