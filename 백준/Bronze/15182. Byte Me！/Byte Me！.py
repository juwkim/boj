g = lambda: [*map(int, input().split())]

N = int(input())
bites = [g() for _ in range(N)]
parity = g()

byte_check = [sum(line) % 2 for line in bites]
if byte_check.count(0) == 1:
    print('Odd')
    bite = byte_check.index(0) + 1
else:
    print('Even')
    bite = byte_check.index(1) + 1

bites.append(parity)
bits = [*map(list, zip(*bites))]
bit_check = [sum(line) % 2 for line in bits]
if bit_check.count(0) == 1:
    bit = bit_check.index(0) + 1
else:
    bit = bit_check.index(1) + 1


print(f'Byte {bite} is broken')
print(f'Bit {bit} is broken')