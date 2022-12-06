alpha = '_abcdefghijklmnopqrstuvwxyz.'
dic = {alpha[i]: i for i in range(28)}
while (s:= input()) != '0':
    k, msg = s.split()
    n, k = len(msg), int(k)
    msg = [dic[c] for c in msg]
    ans = [0 for _ in range(n)]
    for i in range(n):
        ans[k * i % n] = alpha[(msg[i] + i) % 28]
    print(*ans, sep='')