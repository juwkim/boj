def count_changes(start_upper):
    changes = 0
    for i, c in enumerate(letters):
        should_be_upper = (i % 2 == 0) if start_upper else (i % 2 == 1)
        if should_be_upper and not c.isupper():
            changes += 1
        elif not should_be_upper and not c.islower():
            changes += 1
    return changes

S = input()

letters = []
indices = []

for i, c in enumerate(S):
    if c.isalpha():
        letters.append(c)
        indices.append(i)

start_upper = count_changes(True) <= count_changes(False)
T = list(S)
for i, c in enumerate(letters):
    should_be_upper = (i % 2 == 0) if start_upper else (i % 2 == 1)
    if should_be_upper:
        T[indices[i]] = c.upper()
    else:
        T[indices[i]] = c.lower()
print("".join(T))