import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
g()
A = {*g()}
B = {*g()}
print(len(A - B) + len(B - A))