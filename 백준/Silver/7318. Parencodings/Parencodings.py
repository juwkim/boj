import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cnt, p = 0, []
    for num in map(int, input().split()):
        for _ in range(num - cnt):
            p.append('(')
        p.append(')')
        cnt = num
    st = []
    for i, c in enumerate(p):
        if c == '(':
            st.append(i)
        else:
            print((i + 1 - st.pop()) // 2, end=' ')
    print()