n, d = map(int, input().split())
print('+---------------------+')

line = '|' + '...' * (d - 1)

i = 1
while i <= min(n, 8 - d):
    line += f'..{i}'
    i += 1
line += '.' * (22 - len(line)) + '|'
print(line)

while n - i >= 6:
    line = '|'
    last = min(n, i + 6)
    while i <= last:
        num = str(i)
        line += '.' * (3 - len(num)) + num
        i += 1
    line += '|'
    print(line)

if i < n:
    line = '|'
    while i <= n:
        num = str(i)
        line += '.' * (3 - len(num)) + num
        i += 1
    line += '.' * (22 - len(line)) + '|'
    print(line)
print('+---------------------+')