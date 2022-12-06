import sys
input = lambda: sys.stdin.readline().rstrip('\n')

cnt = 1
while (s := input()) != '0':
    N, S = s.split()
    dic = {c: i for i, c in enumerate(S)}
    buf = [input() for _ in range(int(N))]
    buf.sort(key=lambda x: [dic[x[i]] for i in range(len(x))])
    print('year', cnt)
    for word in buf:
        print(word)
    cnt += 1