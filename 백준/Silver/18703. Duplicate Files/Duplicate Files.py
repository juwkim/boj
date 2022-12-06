import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        name, ID = input().split()
        if name in dic:
            dic[name] = min(dic[name], int(ID))
        else:
            dic[name] = int(ID)
    print(*sorted(dic.values()))