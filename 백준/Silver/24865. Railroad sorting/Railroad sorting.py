n, *a = map(int, open(0).read().split())
one, two = [], []
for num in a:
    if num&1:
        one.append(num)
        print(1)
    else:
        two.append(num)
        print(2)
for i in range(1, n + 1):
    if i & 1:
        cnt = 0
        while one[-1] != i:
            two.append(one.pop())
            print(12)
            cnt += 1
        one.pop()
        print(-1)
        for _ in range(cnt):
            one.append(two.pop())
            print(21)
    else:
        cnt = 0
        while two[-1] != i:
            one.append(two.pop())
            print(21)
            cnt += 1
        two.pop()
        print(-2)
        for _ in range(cnt):
            two.append(one.pop())
            print(12)