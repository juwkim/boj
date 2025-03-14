_, *l, _ = open(0).read().replace('\r', '').split('\n')
log = []
for s in l:
    if s[0] == 'R':
        log.append(s[4:])
        print(s[4:])
    else:
        p = (len(log) - 1 - s.count('+')) % len(log)
        print(log[p])
        log.append(log.pop(p))