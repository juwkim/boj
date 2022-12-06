import re
input()
a = [s.start() for s in re.finditer('[.]', input())]
print(min(a[i+1] - a[i] for i in range(len(a) - 1)) - 1)