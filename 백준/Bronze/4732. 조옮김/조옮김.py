scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
scale_idx = {'A': 0, 'A#': 1, 'Bb': 1, 'B': 2, 'B#': 3, 'C': 3, 'C#': 4, 'Db': 4, 'D': 5, 'D#': 6, 'Eb': 6, 'E': 7, 'Fb': 7, 'E#': 8, 'F': 8, 'F#': 9, 'Gb': 9, 'G': 10, 'G#': 11}

while (s:= input()) != '***':
    tones = s.split()
    n = int(input())
    print(*[scale[(scale_idx[tone] + n) % 12] for tone in tones])