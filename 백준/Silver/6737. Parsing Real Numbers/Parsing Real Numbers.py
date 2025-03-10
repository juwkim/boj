import re

p = re.compile(r'^[-+]?\d+(\.\d+)?([eE][-+]?\d+)?$')
for _ in range(int(input())):
    if p.match(input().strip()):
        print("LEGAL")
    else:
        print("ILLEGAL")