import re
# s = 'ABC3721D86'
s = 'A83C721D8E67'

def convert(value):
    matched = value.group()
    if int(matched) >=6:
        return '9'
    else:
        return '0'
r = re.sub('\d',convert,s)
print(r)