buf = input().split(' ')
s, cur = 0, 0
while cur < len(buf):
    if len(buf[cur]) < 1:
        pass
    elif buf[cur] == 'What':
        s = cur
    elif buf[cur][-1] == '?':
        buf[s] = 'Forty-two'
        print(*buf[s:cur], end=' ')
        print(buf[cur][:-1] + '.')
    cur += 1