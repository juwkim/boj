import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    G, P = g()
    if G == 0:
        break
    orders = [g() for _ in range(G)]
    for _ in range(int(input())):
        K, *nums = g()
        score = [0] * P
        for order in orders:
            for i in range(P):
                if order[i] <= K:
                    score[i] += nums[order[i] - 1]
        Max = max(score)
        print(*[i + 1 for i in range(P) if score[i] == Max])