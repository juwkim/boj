import sys
input = lambda: sys.stdin.readline().rstrip()

dic2 = {"at": "@", "to": "2", "be": "b", "oh": "o"}
dic3 = {"and": "&", "one": "1", "won": "1", "too": "2", "two": "2", "for": "4", "bea": "b", "bee": "b", "sea": "c", "see": "c", "eye": "i", "owe": "o", "are": "r", "you": "u", "why": "y"}
dic4 = {"four": "4"}

for _ in range(int(input())):
    s = input()
    i = 0
    while i < len(s):
        if s[i] == ' ':
            print(" ", end="")
            i += 1
        elif i + 3 < len(s) and s[i:i + 4].lower() in dic4:
            if s[i].isupper():
                print(dic4[s[i:i + 4].lower()].upper(), end="")
            else:
                print(dic4[s[i:i + 4].lower()], end="")
            i += 4
        elif i + 2 < len(s) and s[i:i + 3].lower() in dic3:
            if s[i].isupper():
                print(dic3[s[i:i + 3].lower()].upper(), end="")
            else:
                print(dic3[s[i:i + 3].lower()], end="")
            i += 3
        elif i + 1 < len(s) and s[i:i + 2].lower() in dic2:
            if s[i].isupper():
                print(dic2[s[i:i + 2].lower()].upper(), end="")
            else:
                print(dic2[s[i:i + 2].lower()], end="")
            i += 2
        else:
            print(s[i], end="")
            i += 1
    print()