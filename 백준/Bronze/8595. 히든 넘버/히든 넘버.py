import re
input()
print(sum(map(int, re.findall('[\d]+', input()))))