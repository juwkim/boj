input = __import__('sys').stdin.readline
dic = {}
while s:= input().rstrip():
    v, k = s.split()
    dic[k] = v
while s:= input().rstrip():
    print(dic.get(s, 'eh'))