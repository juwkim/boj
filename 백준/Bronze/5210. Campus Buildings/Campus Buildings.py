for i in range(1, 1 + int(input())):
    words = []
    for _ in range(int(input())):
        words.append(input())
    target = input().lower()
    print(f'Data Set {i}:')
    for word in words:
        flag = True
        start = -1
        p = word.lower()
        for c in target:
            start = p.find(c, start + 1)
            if start == -1:
                flag = False
                break
        if flag:
            print(word)