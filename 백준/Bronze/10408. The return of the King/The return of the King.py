S = input()
zeros = S.count('0')
print(f'{(sum(map(int, S)) + 9 * zeros) / (len(S) - zeros):.2f}')