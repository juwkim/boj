from collections import defaultdict
dic = defaultdict(list)
for _ in range(int(input())):
    mentor, mentee = input().split()
    dic[mentor].append(mentee)
for mentor in sorted(dic):
    for mentee in sorted(dic[mentor], reverse=True):
        print(mentor, mentee)