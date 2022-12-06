S, N = int(input()), int(input())
text = input()
i, count, check = 0, 0, 0
N -= 2
while i < N:
    if text[i:i+3] == "IOI":
        i += 2
        check += 1
        count += check >= S
    else:
        i += 1
        check = 0
print(count)