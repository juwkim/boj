import sys
input = lambda: sys.stdin.readline().rstrip()

words = [input() for _ in range(int(input()))]
dic = set(words)

for _ in range(int(input())):
    s = input()
    if s in dic:
        ans = f"{s} is correct"
    else:
        ans = f"{s} is unknown"
        for word in words:
            if len(s) == len(word):
                diff = sum(a != b for a, b in zip(s, word))
                if diff == 1:
                    ans = f"{s} is a misspelling of {word}"
                    break
                if diff == 2:
                    i1, i2 = [i for i in range(len(s)) if s[i] != word[i]]
                    if s[i1] == word[i2] and s[i2] == word[i1]:
                        ans = f"{s} is a misspelling of {word}"
                        break
            elif len(s) == len(word) - 1:
                i = 0
                while i < len(s) and s[i] == word[i]:
                    i += 1
                while i < len(s) and s[i] == word[i + 1]:
                    i += 1
                if i == len(s):
                    ans = f"{s} is a misspelling of {word}"
                    break
            elif len(s) == len(word) + 1:
                i = 0
                while i < len(word) and s[i] == word[i]:
                    i += 1
                while i < len(word) and s[i + 1] == word[i]:
                    i += 1
                if i == len(word):
                    ans = f"{s} is a misspelling of {word}"
                    break
    print(ans)