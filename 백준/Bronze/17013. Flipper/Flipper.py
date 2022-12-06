one = [0, 0]
for move in input():
    one[move == 'V'] ^= 1
vuf = ['1 2\n3 4', '3 4\n1 2', '2 1\n4 3', '4 3\n2 1']
print(vuf[one[0] + 2 * one[1]])