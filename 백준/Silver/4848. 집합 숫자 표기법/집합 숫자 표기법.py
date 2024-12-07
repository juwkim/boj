get = lambda s: s[::-1].index('{') - 1
for _ in range(int(input())):
    num = get(input()) + get(input())
    l = ["{}"]
    for i in range(1, num + 1):
        l.append("{" + ",".join(l) + "}")
    print(l[num])