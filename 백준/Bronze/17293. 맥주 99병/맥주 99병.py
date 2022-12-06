N = int(input())
T = N
while N > 2:
    print(f'{N} bottles of beer on the wall, {N} bottles of beer.')
    N -= 1
    print(f'Take one down and pass it around, {N} bottles of beer on the wall.\n')

if N == 2:
    print(f'{N} bottles of beer on the wall, {N} bottles of beer.')
    N -= 1
    print(f'Take one down and pass it around, {N} bottle of beer on the wall.\n')

if N == 1:
    print('1 bottle of beer on the wall, 1 bottle of beer.')
    print('Take one down and pass it around, no more bottles of beer on the wall.\n')
    print('No more bottles of beer on the wall, no more bottles of beer.')
    if T > 1:
        print(f'Go to the store and buy some more, {T} bottles of beer on the wall.')
    else:
        print(f'Go to the store and buy some more, {T} bottle of beer on the wall.')