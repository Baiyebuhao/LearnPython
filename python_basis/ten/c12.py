# 组()代表组
import re
a = 'PythonPythonPythonPythonPython'
# 4~8
r1 = re.findall('(Python){3}(JS)',a)
# [abc] 或关系 （abc）且关系
print(r1)