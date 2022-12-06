for i,a in enumerate(bin(int(input()))[2:][::-1]):
    if int(a):
        print(i,end=' ')