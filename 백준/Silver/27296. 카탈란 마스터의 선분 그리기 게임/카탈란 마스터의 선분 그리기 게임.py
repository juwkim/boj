for l in [*open(0)][1:]:
    if int(l) < 2:
        print(1, 0)
    else:
        print(0, 1)