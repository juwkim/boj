buf = []
x, y = -1, -1
N = int(input())
for i in range(1, 1 + N):
    line = input()
    if y == -1:
        x, y = i, line.find("*")
    buf.append(line)

l_hand = y - buf[x].find('*')
r_hand = buf[x].rfind('*') - y
buf = [*zip(*buf)]
waist = buf[y].count('*') - 2
l_leg = buf[y - 1].count('*') - 1
r_leg = buf[y + 1].count('*') - 1


print(x + 1, y + 1)
print(l_hand, r_hand, waist, l_leg, r_leg)