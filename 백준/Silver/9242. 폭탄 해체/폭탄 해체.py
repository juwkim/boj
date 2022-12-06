dic = {'******   ******': 0, '          *****': 1, '***    *  *****': 4, '* **** * **** *': 2, '* * ** * ******': 3, '****** * ** ***': 6, '*** ** * ** ***': 5, '*** ** * ******': 9, '*    *    *****': 7, '****** * ******': 8}
buf = [input() for _ in range(5)]
l = (max(map(len, buf)) + 3) // 4 * 4
for i in range(5):
    buf[i] = buf[i] + ' ' * (l - len(buf[i]))
tmp = [''.join(line) for line in zip(*buf)]
lines = []
for i in range(0, l, 4):
    lines.append(tmp[i] + tmp[i+1] + tmp[i+2])

num = 0
for line in lines:
    if dic.get(line) != None:
        num = num * 10 + dic.get(line)
    else:
        num = False
        break
if num and num % 6 == 0:
    print('BEER!!')
else:
    print('BOOM!!')