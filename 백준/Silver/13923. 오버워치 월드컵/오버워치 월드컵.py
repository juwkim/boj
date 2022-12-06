from collections import defaultdict
while True:
    try:
        N = int(input())
        dic = defaultdict(list)
        for i in range(1, 1 + N):
            for j, c in enumerate(input(), 1):
                dic[c].append((i, j))
        for k, v in dic.items():
            if len(v) == N - 1:
                c = k
            elif len(v) == 1:
                i, j = v.pop()
            elif len(v) == N + 1:
                a, b = zip(*v)
                for x in range(N + 1):
                    if a.count(a[x]) == 2 and b.count(b[x]) == 2:
                        i, j = a[x], b[x]
                        break                    
        print(i, j, c)
    except:
        break