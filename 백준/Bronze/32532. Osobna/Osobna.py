OIB = input()[15:26]
s = input()
y, m, d = s[:2], s[2:4], s[4:6]
if y > "24": y = "19" + y
else:        y = "20" + y
name, last_name = input().replace("<", " ").split()
print(f"Ime: {name.capitalize()}")
print(f"Prezime: {last_name.capitalize()}")
print(f"Datum rodjenja: {d:02}-{m:02}-{y}")
print(f"OIB: {OIB}")