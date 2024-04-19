print("         HERD     ADULT     ADULT     MALE     FEMALE     MALE     FEMALE")
print("YEAR     SIZE     MALES    FEMALES    FAWNS     FAWNS    NEWBORN   NEWBORN")
print("----   -------   -------   -------   -------   -------   -------   -------")
female, male = [1280, 640, 3714], [1372, 686, 1703]
for y in range(1994, 1994 + int(input())):
    print(f"{y} {sum(female) + sum(male): 9d} {male[2]: 9d} {female[2]: 9d} {sum(male[:2]): 9d} {sum(female[:2]): 9d} {male[0]: 9d} {female[0]: 9d}")
    new_male = [0, 0, 0]
    new_female = [0, 0, 0]
    new_male[0] = (female[2] * 78 + 50) // 100
    new_female[0] = (female[2] * 72 + 50) // 100
    new_male[1] = (male[0] * 55 + 50) // 100
    new_female[1] = (female[0] * 55 + 50) // 100
    new_male[2] = (male[2] * 3 + male[1] * 12 + 10) // 20
    new_female[2] = (female[2] * 9 + female[1] * 6 + 5) // 10
    male = new_male
    female = new_female