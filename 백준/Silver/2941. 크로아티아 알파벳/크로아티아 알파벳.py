croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for alphabet in croatian:
    word = word.replace(alphabet, 'a')
print(len(word))