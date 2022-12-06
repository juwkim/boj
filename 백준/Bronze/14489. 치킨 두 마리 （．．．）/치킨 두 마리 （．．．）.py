A, B = map(int, input().split())
C = int(input())
print(A + B - 2 * C * (A + B >= 2 * C))