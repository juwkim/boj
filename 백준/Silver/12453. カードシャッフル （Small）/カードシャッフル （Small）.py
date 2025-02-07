import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, 1 + int(input())):
    M, C, W = g()
    card = [*range(1, M + 1)]
    for _ in range(C):
        A, B = g()
        card = card[A-1:A+B-1] + card[:A-1] + card[A+B-1:]
    print(f'Case #{tc}: {card[W-1]}')