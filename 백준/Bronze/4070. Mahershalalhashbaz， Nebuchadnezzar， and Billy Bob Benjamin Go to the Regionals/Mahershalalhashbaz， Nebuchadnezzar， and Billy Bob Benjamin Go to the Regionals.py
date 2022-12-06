cnt = 1
while (s:= input()) != '0 0':
    n, k = map(int, s.split())
    names = sorted(len(input()) for _ in range(n))
    flag = 'yes'
    for i in range(0, n, k):
        m = sum(names[i:i+k]) / k
        if any(abs(leng - m) > 2 for leng in names[i:i+k]):
            flag = 'no'
            break

    print(f'Case {cnt}: {flag}\n')
    cnt += 1