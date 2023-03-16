while True:
    try:
        s = input()
        
        ans = []
        check = set()
        for l in range(1, len(s) + 1):
            for j in range(len(s) + 1 - l):
                tmp = s[j:j+l]
                if tmp in check:
                    continue
                check.add(tmp)
                if tmp == tmp[::-1]:
                    ans.append('"' + tmp + '"')
        print(len(ans), '-', *ans)
    except:
        break