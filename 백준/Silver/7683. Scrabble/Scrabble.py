from collections import Counter
while N:= int(input()):
    words = [input() for _ in range(N)]
    
    ans = 0
    tiles = Counter(input())
    for word in words:
        cnt = Counter(word)
        num = sum(max(0, cnt[c] - tiles[c]) for c in cnt)
        ans += num <= tiles['_']
    print(ans)