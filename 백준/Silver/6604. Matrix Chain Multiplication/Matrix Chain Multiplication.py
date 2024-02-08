import sys
input = lambda: sys.stdin.readline().rstrip()

mat = {}
for _ in range(int(input())):
    c, a, b = input().split()
    mat[c] = (int(a), int(b))

while True:
    l = input()
    if not l:
        break
    st, ans, buf = 0, 0, []
    for c in l:
        if c == ')':
            if st == 0 or len(buf) < 2:
                ans = "error"
                break
            b, a = buf.pop(), buf.pop()
            if a[1] != b[0]:
                ans = "error"
                break
            ans += a[0] * a[1] * b[1]
            st -= 1
            buf.append((a[0], b[1]))
        elif c == '(':
            st += 1
        else:
            buf.append(mat[c])
    if ans != "error":
        print(ans)
    else:
        print("error")