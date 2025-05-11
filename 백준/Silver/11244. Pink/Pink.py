import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

for _ in range(int(input())):
    dic = defaultdict(set)
    for i in range(int(input())):
        s = input()
        if len(s) == 44:
            for j in range(35):
                dic[s[j:j+10]].add(i)
        else:
            match len(dic[s]):
                case 0:
                    print("not exist")
                case 1:
                    print("unique")
                case _:
                    print("duplicate")