import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    F, tosses = input().split()
    print(f"Case #{tc}: {(1 + float(F) / 2) ** int(tosses)}")