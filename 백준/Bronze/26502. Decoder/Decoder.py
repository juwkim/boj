for _ in range(int(input())):
    txt = input()
    table = txt.maketrans("yaeiouYAEIOU", "aeiouyAEIOUY")
    print(txt.translate(table))