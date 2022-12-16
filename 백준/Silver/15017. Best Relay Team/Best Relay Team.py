N = int(input())
buf = []
for _ in range(N):
    name, *l = input().split()
    first, second = map(float, l)
    buf.append((name, first, second))
first = sorted(buf, key=lambda x: x[1])
second = sorted(buf, key=lambda x: x[2])

total, front, ans = 1e9, '', []
for i in range(4):
    num, one, tmp, k = 0, '', [], 0
    while len(tmp) + (one != '') != 4:
        if len(tmp) + (one != '') == i:
            j = 0
            while first[j][0] in tmp:
                j += 1
            num += first[j][1]
            one = first[j][0]
        else:
            while len(tmp) + (one != '') != i and len(tmp) + (one != '') != 4:
                if second[k][0] != one:
                    num += second[k][2]
                    tmp.append(second[k][0])
                k += 1
    if num < total:
        total = num
        ans = tmp
        front = one
print(total)
print(front)
for name in ans:
    print(name)