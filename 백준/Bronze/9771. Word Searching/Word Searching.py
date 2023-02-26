ans = 0
word = input()
while True:
    try:
        line = input()
        ans += line.count(word)
    except:
        break
print(ans)