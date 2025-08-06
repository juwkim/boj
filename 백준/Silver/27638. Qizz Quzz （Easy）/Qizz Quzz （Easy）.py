import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    def solve():
        input()
        n = int(input())
        ls = input().split()
        i = 0
        dic = {}
        while i < n and ((ls[i].isdigit() and not ls[i].startswith('0') and int(ls[i]) == i + 1) or (ls[i].isalpha() and ls[i].islower() and (len(ls[i]) == 4 or len(ls[i]) == 8))):
            if len(dic) != 2 and not ls[i].isdigit():
                if len(dic) == 0:
                    if len(ls[i]) == 8:
                        return i
                    dic[i + 1] = ls[i]
                elif len(ls[i]) == 4:
                    if (i + 1) % list(dic.keys())[0]:
                        dic[i + 1] = ls[i]
                elif ls[i][:4] not in dic.values():
                    return i
                else:
                    dic[i + 1] = ls[i][4:]
            i += 1
        
        kvs = sorted(dic.items())
        for j, l in enumerate(ls[:i], 1):
            s = ""
            for k, v in kvs:
                if j % k == 0:
                    s += v
            if s == l or (s == "" and l.isdigit()):
                continue
            return j - 1
        return i
    print(solve())