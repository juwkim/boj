a = sorted(input().replace(' ', ''))
b = sorted(input().replace(' ', ''))
print(['Is not an anagram.', 'Is an anagram.'][a == b])