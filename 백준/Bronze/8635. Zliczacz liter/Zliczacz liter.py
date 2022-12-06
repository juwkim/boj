from collections import Counter
s = []
for i in range(int(input())):
    s += [*input()]
for l in sorted(Counter(s).items(), key=lambda a:(a[0].isupper(), a[0])):
    if l[0] != ' ':
        print(*l)