import sys
input = sys.stdin.readline

def solve(i, scores, total_sum):
    lo, hi = 0, 1
    for _ in range(100):
        mid = (lo + hi) / 2
        my_score = scores[i] + total_sum * mid
        if sum(max(0, (my_score - scores[j]) / total_sum) for j in range(len(scores))) > 1:
            hi = mid
        else:
            lo = mid
    return lo * 100

for tc in range(1, int(input()) + 1):
    N, *scores = map(int, input().split())
    total_sum = sum(scores)
    print(f"Case #{tc}:", end=' ')
    for i in range(N - 1):
        print(solve(i, scores, total_sum), end=' ')
    print(solve(N - 1, scores, total_sum))