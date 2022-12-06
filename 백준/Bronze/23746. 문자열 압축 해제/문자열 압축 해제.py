import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]
dic = {}
for _ in range(int(input())):
    val, key = input().rstrip().split()
    dic[key] = val
con = ''.join([dic[i] for i in input().rstrip()])
S, E = g()
print(con[S-1:E])