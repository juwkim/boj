s = input()
print(k if (k:=sum('i' not in ''.join(map(lambda x: chr(97+(ord(x)+i-97)%26), s)) for i in range(26))) else 'impossible')