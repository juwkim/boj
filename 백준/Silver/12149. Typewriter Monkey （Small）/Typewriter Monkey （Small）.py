import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import Counter
from itertools import product

def count_occurrences(s, target):
    count = 0
    for i in range(len(s) - len(target) + 1):
        count += s[i:i+len(target)] == target
    return count

def get_overlap(target):
    for i in range(1, len(target)):
        if target.startswith(target[i:]):
            return len(target) - i
    return 0

for tc in range(1, int(input()) + 1):
    K, L, S = map(int, input().split())
    keyboard = Counter(input())
    target = input()
    if any(c not in keyboard for c in target):
        print(f"Case #{tc}: 0")
        continue
    prob = {c: keyboard[c] / K for c in keyboard}
    overlap = get_overlap(target)
    bananas = (S - overlap) // (L - overlap)
    for word in map(''.join, product(keyboard, repeat=S)):
        p = 1
        for c in word: p *= prob[c]
        bananas -= count_occurrences(word, target) * p
    print(f"Case #{tc}: {bananas}")