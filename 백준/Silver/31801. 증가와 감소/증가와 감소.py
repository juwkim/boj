import sys
input = sys.stdin.readline

px = [0] * 1000001
for i in range(120, 1000001):
    s = str(i)
    idx = max(range(1, len(s) - 1), key=lambda x: s[x])
    px[i] = px[i - 1] + (all(s[j] < s[j + 1] for j in range(idx)) and all(s[j] > s[j + 1] for j in range(idx, len(s) - 1)))
    
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(px[b] - px[a - 1])