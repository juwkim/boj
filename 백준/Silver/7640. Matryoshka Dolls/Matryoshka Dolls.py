from collections import Counter
while N:= int(input()):
    cnt = Counter(int(input()) for _ in range(N))
    ans = max(cnt.values())
    print(ans)