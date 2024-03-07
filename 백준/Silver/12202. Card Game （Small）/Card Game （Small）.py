import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, K = g()
    st = []
    for a in g():
        if len(st) >= 2 and st[-1] == st[-2] == a:
            st.pop()
            st.pop()
        else:
            st.append(a)
    print(f'Case #{tc}: {len(st)}')