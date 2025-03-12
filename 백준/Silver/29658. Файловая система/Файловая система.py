import re

def is_valid(s):
    if re.sub(r"[A-Z0-9'\-!#\$%&()@^_`{}.~]", "", s) != "" or s.count('.') > 1:
        return False
    if '.' in s:
        return len(s) - 4 <= s.index('.') <= 8
    return len(s) <= 8

def solve():
    file_name = input().upper()
    if is_valid(file_name):
        return file_name
    file_name = ''.join('_' if c in "\"/\\[]:;=," else c for c in file_name.replace(" ", "")).rstrip('.')
    idx = file_name.rfind('.')
    if idx == -1:
        file_name = file_name[:6] + "~1"
    else:
        s1 = file_name[:idx].replace('.', '')
        s2 = file_name[idx + 1:]
        file_name = s1[:6] + "~1." + s2[:3]
    return file_name
print(solve())