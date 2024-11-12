l = len(s:=input()) >> 1
if l & 1 and s[l] == '+' and s[0] != '0' and s[:l].isdigit() and s[:l] == s[-l:]:
    print('CUTE')
else:
    print("No Money")