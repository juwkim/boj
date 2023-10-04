import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    E, TO = g()
    user = set()
    dic, cnt = {}, 0
    for _ in range(E):
        l = input().split()
        if len(l) == 3:
            dic = {}
        else:
            time, _, name, action = l
            if action == "LOG_IN":
                user.add(name)
                h, m = map(int, time.split(":"))
                t = h * 60 + m
                dic[name] = t
                for name in tuple(dic.keys()):
                    if (t - dic[name]) % 1440 >= TO:
                        del dic[name]
                cnt = max(cnt, len(dic))
            else:
                if name in dic:
                    del dic[name]
    print(len(user), cnt)