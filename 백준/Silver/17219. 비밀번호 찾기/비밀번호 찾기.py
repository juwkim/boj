import sys
input = sys.stdin.readline
passwords = {}
N, M = map(int, input().split())
for _ in range(N):
    site, password = input().rstrip().split()
    passwords[site] = password
for _ in range(M):
    print(passwords[input().rstrip()])