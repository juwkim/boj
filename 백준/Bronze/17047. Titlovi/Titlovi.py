nums = []
times = []
articles = []
lasts = []
while True:
    nums.append(input())
    times.append(input())
    buf = []
    while (s:= input()) not in '#':
        buf.append(s)
    articles.append(buf)
    lasts.append(s)
    if s == '#':
        break
T = int(input())
for num, time, article, last in zip(nums, times, articles, lasts):

    t1, t2 = time.split(' --> ')
    h1, m1, s1, u1 = int(t1[:2]), int(t1[3:5]), int(t1[6:8]), int(t1[9:])
    h2, m2, s2, u2 = int(t2[:2]), int(t2[3:5]), int(t2[6:8]), int(t2[9:])
    t1 = ((h1 * 60 + m1) * 60 + s1) * 1000 + u1 + T
    t2 = ((h2 * 60 + m2) * 60 + s2) * 1000 + u2 + T
    
    t1, u1 = divmod(t1, 1000)
    t1, s1 = divmod(t1, 60)
    h1, m1 = divmod(t1, 60)
    
    t2, u2 = divmod(t2, 1000)
    t2, s2 = divmod(t2, 60)
    h2, m2 = divmod(t2, 60)
    
    print(num)
    print('%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d' % (h1, m1, s1, u1, h2, m2, s2, u2))
    print(*article, sep='\n')
    print(last)