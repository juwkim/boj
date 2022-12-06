import sys
input = sys.stdin.readline
N = int(input())
M = input().rstrip()
K = int(input())
print('NO' if any(M[i] == '1' for i in range(max(0, N-K), N)) else 'YES')