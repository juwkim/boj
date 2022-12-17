buf = []
while (s:= input().split())[0] != 'Waterloo':
    buf.append(s)
ans = min(buf, key=lambda x: int(x[1]))
print(ans[0])