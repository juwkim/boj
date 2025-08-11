dic = {
    'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
    'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
    'UAU':'Tyr','UAC':'Tyr',
    'UGU':'Cys','UGC':'Cys',            'UGG':'Trp',
    'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
    'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
    'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
    'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
    'AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met',
    'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
    'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
    'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
    'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
    'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
    'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
    'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'
}

def translate_mrna(mrna):
    start = mrna.find('AUG')
    if start == -1:
        return []
    codons = []
    i, good = start + 3, False
    while i + 2 < len(mrna):
        codon = mrna[i:i+3]
        if codon in {'UAA', 'UAG', 'UGA'}:
            good = True
            break
        codons.append(dic[codon])
        i += 3
    if not good:
        return []
    return codons

for l in map(str.rstrip, [*open(0)][:-1]):
    s = l.replace('T', 'U')
    t = s.translate(str.maketrans({'A':'U', 'U':'A', 'C':'G', 'G':'C'}))
    ans = "*** No translatable DNA found ***"
    for mrna in s, s[::-1], t[::-1], t:
        codons = translate_mrna(mrna)
        if codons:
            ans = '-'.join(codons)
            break
    print(ans)