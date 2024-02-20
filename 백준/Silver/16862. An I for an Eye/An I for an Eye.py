dic2 = {"at": "@", "to": "2", "be": "b", "oh": "o"}
dic3 = {"and": "&", "one": "1", "won": "1", "too": "2", "two": "2", "for": "4", "bea": "b", "bee": "b", "sea": "c", "see": "c", "eye": "i", "owe": "o", "are": "r", "you": "u", "why": "y"}
dic4 = {"four": "4"}
dic2.update({k.capitalize(): v.capitalize() for k, v in dic2.items()})
dic3.update({k.capitalize(): v.capitalize() for k, v in dic3.items()})
dic4.update({k.capitalize(): v.capitalize() for k, v in dic4.items()})

for _ in range(int(input())):
    s = input()
    i = 0
    while i < len(s):
        if s[i:i + 4] in dic4:
            t = dic4[s[i:i + 4]]
            i += 4
        elif s[i:i + 3] in dic3:
            t = dic3[s[i:i + 3]]
            i += 3
        elif s[i:i + 2] in dic2:
            t = dic2[s[i:i + 2]]
            i += 2
        else:
            t = s[i]
            i += 1
        print(t, end="")
    print()