s = input()
for school_name, password in (("NLCS", "northlondo"), ("BHA", "branksomeh"), ("KIS", "koreainter"), ("SJA", "stjohnsbur")):
    l = set((ord(i) - ord(j)) % 26 for i, j in zip(s, password))
    if len(l) == 1:
        print(school_name)
        break