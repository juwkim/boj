from collections import Counter

N = int(input())
if Counter(input().split()).most_common(1)[0][1] <= (N + 1) // 2:
    print("YES")
else:
    print("NO")