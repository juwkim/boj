import sys
input = lambda: sys.stdin.readline().rstrip()

w = ((3, 1, 1, 1, 1, 1, 1, 3),
     (1, 2, 1, 1, 1, 1, 1, 1),
     (1, 1, 2, 1, 1, 1, 1, 1),
     (1, 1, 1, 2, 1, 1, 1, 1),
     (1, 1, 1, 1, 2, 1, 1, 1),
     (1, 1, 1, 1, 1, 1, 1, 1),
     (1, 1, 1, 1, 1, 1, 1, 1),
     (3, 1, 1, 1, 1, 1, 1, 2))
l = ((1, 1, 1, 2, 1, 1, 1, 1),
     (1, 1, 1, 1, 1, 3, 1, 1),
     (1, 1, 1, 1, 1, 1, 2, 1),
     (2, 1, 1, 1, 1, 1, 1, 2),
     (1, 1, 1, 1, 1, 1, 1, 1),
     (1, 3, 1, 1, 1, 3, 1, 1),
     (1, 1, 2, 1, 1, 1, 2, 1),
     (1, 1, 1, 2, 1, 1, 1, 1))
w = [p + p[:-1][::-1] for p in w]
l = [p + p[:-1][::-1] for p in l]
w += w[:-1][::-1]
l += l[:-1][::-1]
val = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 11}
while (s:=input()) != '#':
    s, word = s.split()
    if s[0].isalpha():
        row, col = int(s[1:]) - 1, ord(s[0]) - ord('A')
        drow, dcol = 1, 0
    else:
        row, col = int(s[:-1]) - 1, ord(s[-1]) - ord('A')
        drow, dcol = 0, 1
    ans, mul = 0, 1
    for c in word:
        mul *= w[row][col]
        ans += l[row][col] * val[c]
        row, col = row + drow, col + dcol
    ans *= mul
    print(s, word, ans)