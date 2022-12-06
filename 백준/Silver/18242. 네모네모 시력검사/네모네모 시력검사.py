input()

while True:
    tmp = input()
    i = tmp.find('#')
    if i != -1:
        S = tmp.count('#')
        break
    
ans = 'DOWN'
if S % 2 == 0:
    ans = 'UP'
else:
    for _ in range(S-2):
        tmp = input()
        if tmp[i] == '.':
            ans = 'LEFT'
            break
        elif tmp[i+S-1] == '.':
            ans = 'RIGHT'
            break
print(ans)