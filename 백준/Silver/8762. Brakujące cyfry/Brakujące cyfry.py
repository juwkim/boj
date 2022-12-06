for _ in range(int(input())):
    ans = []
    for _ in range(int(input())):
        a, b = input().split()
        idx = a.find('x')
        if idx == -1:
            idx = b.find('x')
            a = int(a)
            b = list(b)
            for i in range(10):
                if idx == 0 and i == 0:
                    continue
                b[idx] = str(i)
                if a % int(''.join(b)) == 0:
                    ans.append(i)
                    break
        else:
            b = int(b)
            a = list(a)
            for i in range(10):
                if idx == 0 and i == 0:
                    continue
                a[idx] = str(i)
                if int(''.join(a)) % b == 0:
                    ans.append(i)
                    break   
    print(*ans, sep='')