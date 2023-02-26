S, N = int(input()), int(input())
target = "I" + "OI" * S
text = input()
i, compare = 0, N-2*S
count = 0
while i < compare:
    if target == text[i:i+2*S+1]:
        count += 1
        i += 2
    else:
        i += 1
print(count)