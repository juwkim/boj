import sys
input = lambda: sys.stdin.readline().rstrip()

a = {'b', 'c', 'f', 'h', 'i', 'k', 'n', 'o', 'p', 's', 'u', 'v', 'w', 'y'}
b = {'ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au', 'ba', 'be', 'bh', 'bi', 'bk', 'br', 'ca', 'cd', 'ce', 'cf', 'cl', 'cm', 'cn', 'co', 'cr', 'cs', 'cu', 'db', 'ds', 'dy', 'er', 'es', 'eu', 'fe', 'fl', 'fm', 'fr', 'ga', 'gd', 'ge', 'he', 'hf', 'hg', 'ho', 'hs', 'in', 'ir', 'kr', 'la', 'li', 'lr', 'lu', 'lv', 'md', 'mg', 'mn', 'mo', 'mt', 'na', 'nb', 'nd', 'ne', 'ni', 'no', 'np', 'os', 'pa', 'pb', 'pd', 'pm', 'po', 'pr', 'pt', 'pu', 'ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru', 'sb', 'sc', 'se', 'sg', 'si', 'sm', 'sn', 'sr', 'ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm', 'xe', 'yb', 'zn', 'zr'}

for _ in range(int(input())):
    s = input()
    dp = [1] + [0] * len(s)
    for i in range(len(s)):
        if dp[i] == 0:
            if dp[i + 1] == 0:
                break
            continue
        if s[i] in a: dp[i + 1] = 1
        if i < len(s) - 1 and s[i:i+2] in b: dp[i + 2] = 1
    print(('NO', 'YES')[dp[-1]])