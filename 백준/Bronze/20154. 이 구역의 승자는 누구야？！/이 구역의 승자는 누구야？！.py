a = '32123333113133122212112221'
s = sum(map(lambda x: int(a[ord(x) - 65]), input()))
print(["You're the winner?","I'm a winner!"][s%2])