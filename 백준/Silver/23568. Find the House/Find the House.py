dic = {}
for _ in range(int(input())):
    a, d, b = input().split()
    a, b = map(int, [a, b])
    if d == 'R':
        val = a + b
    else:
        val = a - b
    dic[a] = val
    if dic.get(a) != None:
        start = a


while dic.get(start) != None:
    start = dic.get(start)
print(start)