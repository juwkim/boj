def solve(amount, trees, left, right):

    while right >= left:
        middle = (left + right) // 2
        logged = sum(max(height - middle, 0) * count for height, count in trees)
        if amount == logged:
            return middle
        elif amount < logged:
            left = middle + 1
        else:
            right = middle - 1
    return left - 1

from collections import Counter
N, M = map(int, input().split())
trees = Counter(map(int, input().split()))
print(solve(M, trees.items(), 0, max(trees.keys()) - 1))