import sys
input = lambda: sys.stdin.readline().rstrip()
l_words = []
while (word:= input()) != '#':
    l_words.append(word)
words = set(l_words)

while (s:= input()) != '#':
    if s in words:
        print(f'{s} is correct')
    else:
        print(s, end=': ')
        l = len(s)
        for word in l_words:
            p = len(word)
            if p == l + 1:
                for i in range(p):
                    check = word[:i] + word[i+1:]
                    if check == s:
                        print(word, end=' ')
                        break
            elif p == l:
                buf = [i for i in range(p) if s[i] != word[i]]
                if len(buf) == 1:
                    print(word, end=' ')
            elif p == l - 1:
                for i in range(l):
                    check = s[:i] + s[i+1:]
                    if check == word:
                        print(word, end=' ')
                        break        
        print()