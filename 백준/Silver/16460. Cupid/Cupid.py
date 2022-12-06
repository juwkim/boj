
import sys
input = lambda: sys.stdin.readline().rstrip('\n')

_, c_sex, c_dist = input().split()
c_dist = int(c_dist)

buf = []
for _ in range(int(input())):
    name, sex, dist = input().split()
    dist = int(dist)
    if (sex in c_sex or c_sex in sex) and dist <= c_dist:
        buf.append(name)
buf.sort()
if buf:
    print(*buf, sep='\n')
else:
    print('No one yet')