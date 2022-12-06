lyric = 'baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'.split()
r, q = divmod(int(input()) - 1, 14)
s = lyric[q]
if s[:2] == 'tu':
    p = s.count('ru') + r
    print(s + 'ru' * r if p < 5 else f'tu+ru*{p}')
else:
    print(s)