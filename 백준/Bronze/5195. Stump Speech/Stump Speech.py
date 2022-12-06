for cnt in range(1, 1 + int(input())):
    dic = {}
    n = int(input())
    for _ in range(n):
        word = input()
        dic[word] = int(input())
    
    ans = 0
    msg = input()
    for k, v in dic.items():
        l = len(k)
        for i in range(len(msg) - l + 1):
            match = True
            for j in range(l):
                if k[j] != msg[i+j]:
                    match = False
                    break
            if match: ans += v
    print(f'Data Set {cnt}:')
    print(ans)