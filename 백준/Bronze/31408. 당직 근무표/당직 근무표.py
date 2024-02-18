from collections import Counter

N = int(input())
if max(Counter(input().split()).values()) <= (N + 1) // 2:
    print("YES")
else:
    print("NO")