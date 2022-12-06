dic = {'A#': 'Bb', 'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab',
       'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'}

import sys
cnt = 1
for line in sys.stdin:
    note, tonality = line.split()
    if dic.get(note):
        print(f'Case {cnt}: {dic.get(note)} {tonality}')
    else:
        print(f'Case {cnt}: UNIQUE')
    cnt += 1