import sys
input = sys.stdin.readline
from itertools import product

d = {}
for a, b, c in product(('+', '-', '*', '//'), repeat=3):
    num = eval(s:=f'4 {a} 4 {b} 4 {c} 4')
    d[num] = f'{s} = {num}'.replace('//', '/')
for _ in range(int(input())):
    print(d.get(int(input()), 'no solution'))