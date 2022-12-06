g = lambda: [*map(int, input().split())]

from statistics import Counter

while (s:= input()) != '0 0':
    N, Q = map(int, s.split())
    cnt = Counter()
    for _ in range(N):
        M, *nums = g()
        cnt += Counter(nums)
    res = cnt.most_common()
    buf = []
    i = 0
    if not res or res[0][1] < Q:
        print(0)
    else:
        while i < len(res):
            if res[i][1] == res[0][1]:
                buf.append(res[i][0])
            else:
                break
            i += 1
        if buf:
            print(min(buf))
        else:
            print(0)