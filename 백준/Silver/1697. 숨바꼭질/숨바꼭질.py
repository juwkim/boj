import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]


N, K = g()
visited = [0] * 110000       
def bfs(node):
    buf = [node]
    visited[node] = 1
    
    cnt = 0
    while True:
        next_buf = []
        for cur in buf:

            if cur == K:
                return cnt
            
            for Next in [cur - 1, cur + 1, cur * 2]:
                if 0 <= Next < 110000 and visited[Next] == 0:
                    next_buf.append(Next)
                    visited[Next] = 1
        cnt += 1
        buf = next_buf

print(bfs(N))