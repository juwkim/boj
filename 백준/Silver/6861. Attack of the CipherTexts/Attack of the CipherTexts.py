dic = {b: a for a, b in zip(input(), input())}
chrs = [*map(chr, range(65, 91)), ' ']
check_a = set(chrs) - set(dic.values())
check_b = set(chrs) - set(dic.keys())
if len(check_a) == len(check_b) == 1:
    dic[check_b.pop()] = check_a.pop()
ans = []
for c in input():
    if c in dic:
        ans.append(dic[c])
    else:
        ans.append('.')
print(''.join(ans))