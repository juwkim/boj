import sys

input = sys.stdin.read
def min_initial_strength():
    data = list(map(int, input().split()))
    N = data[0]
    a = data[1:N+1]
    b = data[N+1:2*N+1]
    
    c = [0] * (N + 1)
    d = [0] * N
    for i in range(N):
        c[i+1] = c[i] + b[i]
        d[i] = a[i] - c[i]
    
    leftm = [0] * N
    rightm = [0] * N
    leftm[0] = d[0]
    rightm[N-1] = d[N-1]
    
    for i in range(1, N):
        leftm[i] = max(d[i-1], leftm[i-1])
    
    for i in range(N-2, -1, -1):
        rightm[i] = max(d[i], rightm[i+1])
    
    ans = float('inf')
    for i in range(N):
        k = max(leftm[i] - c[N], rightm[i]) + c[i]
        ans = min(ans, k)
    
    print(ans)

if __name__ == "__main__":
    min_initial_strength()
