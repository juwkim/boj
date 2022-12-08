from collections import Counter
while True:
    try:
        cnt = Counter(input()) & Counter(input())
        for k, v in sorted(cnt.items()):
            print(k * v, end='')
        print()        
    except:
        break