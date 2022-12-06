from collections import Counter
while True:
    try:
        s = input().replace(' ', '')
        if not s:
            break
        length = 1
        while True:
            cnt = Counter([s[i:i+length] for i in range(len(s) - length + 1)])
            num = cnt.most_common(1)[0][1]
            if num == 1:
                break
            print(num)
            length += 1
        print()
    except:
        break