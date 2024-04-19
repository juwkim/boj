print("         HERD     ADULT     ADULT     MALE     FEMALE     MALE     FEMALE")
print("YEAR     SIZE     MALES    FEMALES    FAWNS     FAWNS    NEWBORN   NEWBORN")
print("----   -------   -------   -------   -------   -------   -------   -------")
female, male = (1280, 640, 3714), (1372, 686, 1703)
for y in range(1994, 1994 + int(input())):
    print(f"{y} {sum(female) + sum(male): 9d} {male[2]: 9d} {female[2]: 9d} {sum(male[:2]): 9d} {sum(female[:2]): 9d} {male[0]: 9d} {female[0]: 9d}")
    male = (female[2] * 39 + 25) // 50, (male[0] * 11 + 10) // 20, (male[2] * 3 + male[1] * 12 + 10) // 20
    female = (female[2] * 36 + 25) // 50, (female[0] * 11 + 10) // 20, (female[2] * 9 + female[1] * 6 + 5) // 10