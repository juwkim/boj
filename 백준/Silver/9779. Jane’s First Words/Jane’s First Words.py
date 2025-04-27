import re

pattern = re.compile(r"^da+dd?[iy]$")
for line in map(str.rstrip, open(0)):
    if pattern.fullmatch(line):
        print("She called me!!!")
    else:
        print("Cooing")