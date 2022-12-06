word = input()
r, q = divmod(len(word), 3)

a = '..#...#...*.' * r + '..#.' * q + '.'
b = '.#.#.#.#.*.*' * r + '.#.#' * q + '.'

print(a)
print(b)
for i in range(len(word)):
    if i and i % 3 == 0 or i % 3 == 2:
        print(f'*.{word[i]}.', end='')
    else:
        print(f'#.{word[i]}.', end='')
print('#' if len(word) % 3 else '*')
print(b)
print(a)