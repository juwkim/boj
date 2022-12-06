from collections import*
input()
print(min(Counter(map(int,input().split())).items(),key=lambda x:x[::-1])[0])