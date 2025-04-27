import sys
input = lambda: sys.stdin.readline().rstrip()

participants = []
for _ in range(int(input())):
    name = input()
    first, last = name.split()
    participants.append((last, first, name))
participants.sort()
dic = {name: idx for idx, (_, _, name) in enumerate(participants)}
for _ in range(int(input())):
    idx = dic[input()]
    start = (idx // 3) * 3
    for i in range(start, start + 3):
        if i != idx:
            print(participants[i][2])