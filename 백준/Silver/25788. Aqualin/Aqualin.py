import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A, B = [], []
for _ in range(n):
    line = input().split()
    A.append(line[::2])
    B.append(line[1::2])

def solve(arr):
    cnt = Counter()
    visited = [bytearray(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            num = 1
            visited[i][j] = 1
            st = [(i, j)]
            while st:
                x, y = st.pop()
                for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == arr[i][j]:
                        visited[nx][ny] = 1
                        num += 1
                        st.append((nx, ny))
            cnt[arr[i][j]] = max(cnt[arr[i][j]], num)
    return sum(v * (v - 1) for v in cnt.values()) >> 1
print(solve(A), solve(B))