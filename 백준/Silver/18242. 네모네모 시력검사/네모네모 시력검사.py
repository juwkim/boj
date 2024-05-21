input()
while True:
    s = input()
    i = s.find('#')
    if i != -1:
        cnt = s.count('#')
        break
ans = 'DOWN'
if cnt % 2 == 0: ans = 'UP'
else:
    for _ in range(cnt // 2 - 1): input()
    s = input()
    if s[i] == '.': ans = 'LEFT'
    elif s[i + cnt - 1] == '.': ans = 'RIGHT'
print(ans)