for i in range(1, 1 + int(input())):
    sex, mother, father = input().split(" ")
    
    mother_ft, mother_in = map(int, mother[:-1].split("'"))
    father_ft, father_in = map(int, father[:-1].split("'"))
    
    key = (mother_ft + father_ft) * 12 + mother_in + father_in
    
    if sex == 'B':
        key += 5
    else:
        key -= 5
    key, r = divmod(key, 2)
    
    min_key = key - 4 + r
    max_key = key + 4
    
    q1, r1 = divmod(min_key, 12)
    q2, r2 = divmod(max_key, 12)
    
    print(f'Case #{i}: {q1}\'{r1}" to {q2}\'{r2}"')