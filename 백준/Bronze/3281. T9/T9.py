alpha = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 'G': '4',
         'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5', 'M': '6', 'N': '6',
         'O': '6', 'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8', 'U': '8',
         'V': '8', 'W': '9', 'X': '9', 'Y': '9', 'Z': '9'}
dic = {}
for _ in range(int(input())):
    word = input()
    key = ''.join([alpha[i] for i in word])
    if not dic.get(key):
        dic[key] = word
n = int(input())

key = ''
buf = []
for num in input().split():
    if num == '1':
        if dic.get(key):
            buf.append(dic.get(key))
        else:
            buf.append('*' * len(key))
        key = ''
        buf.append(' ')
    else:
        key += num
if dic.get(key):
    buf.append(dic.get(key))
else:
    buf.append('*' * len(key))

print(*buf, sep='')