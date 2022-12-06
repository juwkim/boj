buf = []
while n:= int(input()):
    buf.append(n)

buf.sort()
ans = ['NIE']
for i in range(len(buf)-3, -1, -1):
    a, b, c = buf[i:i+3]
    if a + b > c:
        ans = [a, b, c]
        break
print(*ans)