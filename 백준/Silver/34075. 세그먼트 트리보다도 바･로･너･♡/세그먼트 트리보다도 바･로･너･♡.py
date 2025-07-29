import sys
input = sys.stdin.readline

algos = []
for _ in range(int(input())):
    name, num = input().split()
    algos.append((int(num), name))
dic = {}
for _ in range(int(input())):
    name, tear = input().split()
    tear = int(tear)
    algo1, algo2 = sorted(algos, key=lambda x: (abs(x[0] - tear), x[1]))[:2]
    dic[name] = f"{algo2[1]} yori mo {algo1[1]}"

name = None
for _ in range(int(input())):
    a, b, c = input().split()
    if b == '-':
        name = a
        print("hai!")
    else:
        print(dic[name])