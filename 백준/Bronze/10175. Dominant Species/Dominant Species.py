from collections import Counter
for _ in range(int(input())):
    location, species = input().split()
    count = Counter(species)
    
    count["B"] *= 2
    count["C"] *= 1
    count["M"] *= 4
    count["W"] *= 3
    
    temp = count.most_common(2)
    if temp[0][1] > temp[1][1]:
        dominant = {'B': 'Bobcat', 'C': 'Coyote', 'M': 'Mountain Lion', 'W': 'Wolf'}[temp[0][0]]
        print(f'{location}: The {dominant} is the dominant species')
    else:
        print(f'{location}: There is no dominant species')