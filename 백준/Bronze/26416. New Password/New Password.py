for step in range(1, 1 + int(input())):
    input()
    S = input()
    if all(i.isupper() == False for i in S):
        S += 'A'
    if all(i.islower() == False for i in S):
        S += 'a'
    if all(i.isdigit() == False for i in S):
        S += '1'
    if all(i not in '#@*&' for i in S):
        S += '#'
    if len(S) < 7:
        S += '1' * (7 - len(S))
    print(f'Case #{step}: {S}')