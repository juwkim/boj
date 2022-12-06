while True:
    try:
        for _ in range(int(input())):
            dic = {}
            cnt = 1
            while s:= input():
                for word in s.split():
                    if word in dic:
                        print(dic[word], end=' ')
                    else:
                        dic[word] = cnt
                        cnt += 1
                        print(word, end=' ')
                print()
            print()
    except:
        break