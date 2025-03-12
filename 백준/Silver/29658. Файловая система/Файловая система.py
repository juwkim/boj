import re

def is_valid_8_3(s):
    if re.sub(r"[A-Z0-9'\-!#\$%&()@^_`{}.~]", "", s) != "" or s.count('.') > 1:
        return False
    if '.' not in s:
        return len(s) <= 8
    return len(s) - 4 <= s.index('.') <= 8

def solve():
    file_name = input().upper()
    
    if is_valid_8_3(file_name):
        return file_name
    
    file_name = file_name.replace(" ", "")
    understike_replace = "\"/\\[]:;=,"
    file_name = ''.join('_' if c in understike_replace else c for c in file_name)
    
    while file_name and file_name[-1] == '.':
        file_name = file_name[:-1]
    
    p = file_name.rfind('.')
    if p != -1:
        s1 = file_name[:p].replace('.', '')
        s2 = file_name[p + 1:]
        file_name = s1[:6] + "~1." + s2[:3]
    else:
        file_name = file_name[:6] + "~1"
    
    return file_name

print(solve())