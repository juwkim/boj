import sys
input = lambda: sys.stdin.readline().rstrip()

name = {}
while not (s:=input()).startswith("000"):
    name[s[:3]] = s[3:]

s = input()
while s[:3] != '000':
    l = [s]
    sss = s[:3]
    while (s:=input())[:3] == sss:
        l.append(s)
    logs, total = [], 0
    for line in l:
        sssnnn, num = line.split()
        num = int(num) / 100
        total -= num
        logs.append((sssnnn[3:], num))
    if total == 0:
        continue
    print(f"*** Transaction {sss} is out of balance ***")
    for log in logs:
        print(f"{log[0]} {name[log[0]]} {log[1]:>{40 - len(name[log[0]])}.2f}")
    print(f"999 Out of Balance {total:>26.2f}\n")