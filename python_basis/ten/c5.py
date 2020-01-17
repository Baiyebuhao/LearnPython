# 概括字符集

# \d  数字0-9  \D  非数字
# \w  单词字符  \W  非单词字符
# \s  空白字符  \S
# . 匹配除换行符\n之外其他所有字符
import re
a = 'python11\11java&___678\php'

r = re.findall('\w',a)   
# r = re.findall('[0-9]',a)
# r = re.findall('^[0-9]',a)
# r = re.findall('[A-Za-z0-9_]',a)
print(r)