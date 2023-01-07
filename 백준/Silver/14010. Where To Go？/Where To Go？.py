N = int(input())
s = input()
for _ in range(N):
    
    station = input()
    idx = 0
    while idx + len(station) <= len(s):
        
        dic = {}
        check = set()
        for a, b in zip(station, s[idx:idx + len(station)]):
            if a not in dic:
                if b in check:
                    break
                dic[a] = b
                check.add(b)
            elif dic[a] != b:
                break
        else:
            break
        idx += 1
    
    if idx + len(station) <= len(s):
        print(idx)
    else:
        print('-')