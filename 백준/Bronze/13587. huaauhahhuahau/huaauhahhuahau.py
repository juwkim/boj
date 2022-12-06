k = [i for i in input() if i in 'aeiou']
print('S' if k == [*reversed(k)] else 'N')