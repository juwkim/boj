import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    k = [*map(int, input().split())]
    ans = [-1] * N
    st = []
    for i in range(N):
        while st and k[st[-1]] < k[i]:
            ans[st.pop()] = i
        st.append(i)
    print(*ans)