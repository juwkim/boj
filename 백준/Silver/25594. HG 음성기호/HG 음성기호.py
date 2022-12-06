hg = {'a': 'aespa', 'b': 'baekjoon', 'c': 'cau', 'd': 'debug', 'e': 'edge',
      'f': 'firefox', 'g': 'golang', 'h': 'haegang', 'i': 'iu', 'j': 'java',
      'k': 'kotlin', 'l': 'lol', 'm': 'mips', 'n': 'null', 'o': 'os',
      'p': 'python', 'q': 'query', 'r': 'roka', 's': 'solvedac', 't': 'tod',
      'u': 'unix', 'v': 'virus', 'w': 'whale', 'x': 'xcode', 'y': 'yahoo',
      'z': 'zebra'}
s = input()
idx, ans = 0, []
while idx < len(s):
    l = hg[s[idx]]
    if idx + len(l) - 1 < len(s) and all(l[i] == s[idx+i] for i in range(len(l))):
        ans.append(s[idx])
        idx += len(l)
    else:
        ans = 'ERROR!'
        break
if ans == 'ERROR!':
    print(ans)
else:
    print("It's HG!")
    print(*ans, sep='')