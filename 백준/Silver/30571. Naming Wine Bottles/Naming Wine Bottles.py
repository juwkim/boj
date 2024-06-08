import sys
input = lambda: sys.stdin.readline().rstrip()

a = 0
dic = {}
for _ in range(int(input())):
    v = float(input()[:-1])
    if v not in dic:
        name = []
        num = a
        while True:
            num, r = divmod(num, 26)
            name.append(chr(r + 97))
            if num == 0:
                break
        dic[v] = ''.join(name)
        a += 1
    print(dic[v])