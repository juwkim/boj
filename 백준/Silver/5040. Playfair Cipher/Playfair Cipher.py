def make_key_map():
    check = {' ', 'Q'}
    mat = [[''] * 5 for _ in range(5)]
    idx = 0
    for c in map(str.upper, input()):
        if c in check:
            continue
        check.add(c)
        mat[idx // 5][idx % 5] = c
        idx += 1
        
    char = 65
    for i in range(idx, 25):
        
        while chr(char) in check:
            char += 1
        
        check.add(chr(char))
        mat[i // 5][i % 5] = chr(char)
    
    return mat

key_map = make_key_map()
idx_map = {}
for i in range(5):
    for j in range(5):
        idx_map[key_map[i][j]] = i, j

text = list(input().replace(' ', '').upper())
ans, idx = [], 0
while idx < len(text):
    if idx == len(text) - 1 or text[idx] == text[idx + 1]:
        text.insert(idx + 1, 'X')
        continue
    
    x1, y1 = idx_map[text[idx]]
    x2, y2 = idx_map[text[idx + 1]]
    
    if x1 == x2:
        ans.append(key_map[x1][(y1 + 1) % 5])
        ans.append(key_map[x2][(y2 + 1) % 5])
    elif y1 == y2:
        ans.append(key_map[(x1 + 1) % 5][y1])
        ans.append(key_map[(x2 + 1) % 5][y2])
    else:
        ans.append(key_map[x1][y2])
        ans.append(key_map[x2][y1])
    
    idx += 2

print(*ans, sep='')