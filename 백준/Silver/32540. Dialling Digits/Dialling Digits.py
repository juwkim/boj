import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

d = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
dic = defaultdict(list)
n, m = map(int, input().split())
for _ in range(n):
    word = input()
    dic[''.join([d[c] for c in word])].append(word)
for _ in range(m):
    s = input()
    print(len(dic[s]), *dic[s])    