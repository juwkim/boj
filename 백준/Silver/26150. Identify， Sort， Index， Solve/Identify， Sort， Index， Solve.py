buf = []
for _ in range(int(input())):
    name, I, D = input().split()
    buf.append((int(I), name[int(D)-1].upper()))
buf.sort()
print(''.join([item[1] for item in buf]))