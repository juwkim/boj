for _ in range(int(input())):
    S = input()
    dotS = S[:(len(S) + 2) // 3]
    taildotS = dotS[1:]
    revdotS = dotS[::-1]
    tailrevdotS = revdotS[1:]
    
    if S == dotS + revdotS + dotS or S == dotS + tailrevdotS + dotS or \
        S == dotS + revdotS + taildotS or S == dotS + tailrevdotS + taildotS:
        print(1)
    else:
        print(0)