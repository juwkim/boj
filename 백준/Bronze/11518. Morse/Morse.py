dic = dict()
for _ in range(26):
    c, morse = input().split()
    dic[c] = morse

words = dict()
for _ in range(int(input())):
    word = input()
    key = ''.join([dic[i] for i in word])
    words[key] = word
while n:= int(input()):
    buf = [input() for _ in range(n)]
    flag = True
    for i in range(n):
        if not words.get(buf[i]):
            print(buf[i], 'not in dictionary.')
            flag = False
            break
        buf[i] = words.get(buf[i])
    if flag:
        print(*buf)