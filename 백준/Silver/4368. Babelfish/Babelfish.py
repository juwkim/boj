input = __import__('sys').stdin.readline
dic = {}
while True:
    s = input().rstrip()
    if len(s) == 0:
        break
    v, k = s.split()
    dic[k] = v
while True:
    try:
        s = input().rstrip()
        if len(s) == 0:
            break
        print(dic.get(s, 'eh'))
    except:
        break