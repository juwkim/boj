import re
room = [input() for _ in range(int(input()))]
a = sum(len(re.findall('[.]{2,}', i)) for i in room)
b = sum(len(re.findall('[.]{2,}', ''.join(i))) for i in zip(*[[*row] for row in room]))
print(a, b)