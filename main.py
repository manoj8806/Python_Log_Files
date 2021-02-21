import re
from collections import Counter

status_codes = []
with open("C:/Users/MANOJ/Downloads/access_log.log", 'r') as f:
    f = f.readlines()
    for line in f:
        m = re.search('HTTP/1.\d" (...)', line)
        status_codes.append(m.group(1))

a = dict(Counter(status_codes))
for key in a:
    print(f'status code {key}->count {a[key]}')