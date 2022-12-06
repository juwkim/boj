N = int(input())
text = input()

check = ['R', 'G', 'B']
i = 0
ans = ''
while True:
    try:
        check.remove(text[i])
        if check == []:
            check = ['R', 'G', 'B']
            ans += text[i]
            if len(ans) == N:
                break
    except:
        pass

    i += 1

print(ans)