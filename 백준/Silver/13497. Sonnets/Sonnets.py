delim = set("-.,:;")
vowel = set("AEIOUYaeiouy")

for cnt in range(1, 1 + int(input())):
    ans = ''
    dic = {}
    rhyme_count = 65
    for _ in range(int(input())):
        line = list(input())
        if line == []:
            ans += ' '
            continue
        for i in range(len(line)):
            if line[i] in delim:
                line[i] = ' '
        line = ''.join(line).split()
        for i in range(len(line) - 1, -1, -1):
            if line[i].isupper():
                idx = i
                break
        line_vowel = [i for i in ''.join(line[idx:]) if i in vowel]
        line_vowel = ''.join(line_vowel)
        if not dic.get(line_vowel):
            dic[line_vowel] = chr(rhyme_count)
            rhyme_count += 1
        ans += dic.get(line_vowel)
    print(f'Data Set {cnt}:\n{ans}\n')