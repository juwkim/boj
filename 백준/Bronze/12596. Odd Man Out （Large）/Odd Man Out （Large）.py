from collections import Counter
for i in range(1, 1+int(input())):
    input()
    for key, value in dict(Counter(map(int, input().split()))).items():
        if value == 1:
            print(f'Case #{i}: {key}')