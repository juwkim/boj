import sys

input = lambda: sys.stdin.readline().rstrip()

input()
dic = {'C': 0, 'O': 0, 'W': 0}
for c in input():
    if c == 'C':
        dic['C'] += 1
    elif c == 'O':
        dic['O'] += dic['C']
    else:
        dic['W'] += dic['O']
print(dic['W'])