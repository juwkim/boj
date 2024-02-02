import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ans = 0
st = []
for c in input():
    if c in "({[":
        st.append(c)
        ans = max(ans, len(st))
    elif not st or st[-1] != {')': '(', '}': '{', ']': '['}[c]:
        ans = "NIE"
        break
    else:
        st.pop()
if st:
    ans = "NIE"
print(ans)