S = list(input())

# a의 아스키 코드 ~ z의 아스키 코드
for i in range(97, 123):
    try:
        print(S.index(chr(i)), end=" ")
    except:
        print(-1, end=" ")