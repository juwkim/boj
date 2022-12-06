A, B, C = map(int, input().split())
I, J, K = map(int, input().split())
s = min(A/I, B/J, C/K)
print(A - s * I, B - s * J, C - s * K)