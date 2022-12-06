l = input().split()        
s = input()
print(sum(i.startswith(s) and len(i) > len(s) for i in l))