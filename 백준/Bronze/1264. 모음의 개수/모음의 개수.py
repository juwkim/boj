from collections import Counter
while(s:=input())!='#':
    a = Counter(s.lower())
    print(sum(a[i] for i in 'aeiou'))