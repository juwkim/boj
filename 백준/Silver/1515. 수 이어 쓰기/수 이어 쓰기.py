import sys

input = lambda: sys.stdin.readline().rstrip()

s = input()
idx = 0
num, s_num = 1, '1'
while idx < len(s):
    for i in range(len(s_num)):
        if s[idx] == s_num[i]:
            idx += 1
            if idx == len(s):
                break
    else:
        num += 1
        s_num = str(num)
        continue
    break
print(num)