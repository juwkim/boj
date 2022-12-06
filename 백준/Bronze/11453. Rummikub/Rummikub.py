for _ in range(int(input())):
    buf = { color: ['0'] * 100 for color in 'rgby'}
    M = int(input())
    tiles = input().split()
    for tile in tiles:
        num, color = int(tile[:-1]) - 1, tile[-1]
        buf[color][num] = '1'
    if any('111' in ''.join(color) for color in buf.values()):
        print('YES')
    elif any(nums.count('1') >= 3 for nums in zip(*buf.values())):
        print('YES')
    else:
        print('NO')