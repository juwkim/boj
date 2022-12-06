a = input().split('|')
minor = sum(note[0] in 'ADE' for note in a)
major = sum(note[0] in 'CFG' for note in a)
print('C-major' if major > minor else 'A-minor' if major < minor else ['C-major', 'A-minor'][a[-1][-1] in 'ADE'])