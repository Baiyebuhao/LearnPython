
import re
lanuage = 'PythonC#JavaC#PHPC#'

def convent(value):
    matched = value.group()
    print(value)
    return '!!' + matched + '!!'

r = re.sub('C#',convent,lanuage,1)
print(r)

