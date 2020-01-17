# 字符集
import re
s = 'abc,acc,adc,aec,afc,ahc'
#找出中间是c或者是f的单词
r = re.findall('a[c-f]c',s)
print(r)