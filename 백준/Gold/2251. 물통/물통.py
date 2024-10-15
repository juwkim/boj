A, B, C = map(int, input().split())
st = [(0, 0, C)]
visited = {(0, 0, C)}
ans = []
while st:
    a, b, c = st.pop()
    if a == 0:
        ans.append(c)
    
    next = max(0, a + b - B), min(a + b, B), c
    if next not in visited:
        visited.add(next)
        st.append(next)
    
    next = max(0, a + c - C), b, min(a + c, C)
    if next not in visited:
        visited.add(next)
        st.append(next)
        
    next = a, max(0, b + c - C), min(b + c, C)
    if next not in visited:
        visited.add(next)
        st.append(next)
    
    next = min(a + b, A), max(0, a + b - A), c
    if next not in visited:
        visited.add(next)
        st.append(next)
    
    next = a, min(b + c, B), max(0, b + c - B)
    if next not in visited:
        visited.add(next)
        st.append(next)
    
    next = min(a + c, A), b, max(0, a + c - A)
    if next not in visited:
        visited.add(next)
        st.append(next)

print(*sorted(ans))