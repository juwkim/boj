while (s:= input()) != '0':
    res = [[] for _ in range(11)]
    buf = []
    for num in map(int, s.split('+')):
        r = num % 10
        if res[10-r]: buf.extend((num, res[10-r].pop()))
        else: res[r].append(num)
    print(*(buf + sum(res, [])), sep='+')