from collections import Counter
while N:= int(input()):
    cnt = Counter(int(input()) for _ in range(N))
    ans = cnt.most_common(1)[0][1]
    print(ans)