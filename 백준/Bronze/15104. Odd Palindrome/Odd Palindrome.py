s=input()
print(['Odd.','Or not.'][any(any(s[j:j+i]==s[j:j+i][::-1]for j in range(len(s)-i))for i in range(2,len(s)+1,2))])