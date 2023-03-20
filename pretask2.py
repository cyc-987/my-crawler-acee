#正则表达式意义
#^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}$
#行始[字母数字下划线或._%+-]一个以上@[字母数字下划线或.-].2-4个大小写字母
#是一个邮箱类似物

import re

str = input('input:')#获得字符串输入
rule = re.compile(r'-?\d+')#构造正则表达式
str_processed = rule.findall(str)#findall方法，返回列表

#str转int列表
list_output = []
for i in str_processed:
    list_output.append(int(i))

print(list_output)