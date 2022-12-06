N = int(input())
count = N
for _ in range(N):
    word = input()
    check = []
    for alphabet in word:
        if alphabet in check and alphabet != check[-1]:
            count -= 1
            break
        if alphabet not in check:
            check.append(alphabet)
print(count)