nn = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
note = {nn[i]: i for i in range(12)}
majorlib, minorlib = {}, {}
for i in range(12):
    vv = sorted((i, (i + 4) % 12, (i + 7) % 12))
    majorlib[nn[vv[0]] + nn[vv[1]] + nn[vv[2]]] = nn[i]
    vv = sorted((i, (i + 3) % 12, (i + 7) % 12))
    minorlib[nn[vv[0]] + nn[vv[1]] + nn[vv[2]]] = nn[i]

for line in open(0):
    chords = line.split()
    if len(chords) != 3:
        break
    vv = []
    for chord in map(str.upper, chords):
        if len(chord) >= 2 and 'B' == chord[1]:
            chord = nn[(note[chord[0]] - 1) % 12]
        vv.append(note[chord])
    vv.sort()
    comb = nn[vv[0]] + nn[vv[1]] + nn[vv[2]]
    if comb in majorlib:
        res = f"a {majorlib[comb]} Major chord."
    elif comb in minorlib:
        res = f"a {minorlib[comb]} Minor chord."
    else:
        res = "unrecognized."
    print(f"{' '.join(chords)} is {res}")