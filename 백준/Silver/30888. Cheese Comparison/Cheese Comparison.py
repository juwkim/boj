n = int(input())
rank = [1] * (n + 1)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        print(f"? {i} {j}", flush=True)
        res = input()
        if res == '<':
            rank[i] += 1
        elif res == '>':
            rank[j] += 1

ans = sorted(range(1, n + 1), key=lambda x: rank[x], reverse=True)
print("!", *ans)