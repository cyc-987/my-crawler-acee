#正则表达式意义
#^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}$
#行始[字母数字下划线或._%+-]一个以上@[字母数字下划线或.-].2-4个大小写字母
#是一个邮箱类似物

import re

str = input('input:')
rule = re.compile(r'-?\d+')
str_processed = rule.findall(str)
#print(str_processed)

list_output = []
for i in str_processed:
    list_output.append(int(i))

print(list_output)