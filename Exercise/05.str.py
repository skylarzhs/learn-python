# python 支持多语言
print('中英文Mixed')

# ord()获取字符的整数表示
print(ord('A'))
print(ord('中'))

# chr()将编码转换成对应的字符
print(chr(65))
print(chr(25991))

# 整数编码
print('\u4e2d\u6587')

# bytes类型的数据表示,b为前缀的单引号或双引号显示。只占用一个字节
print(b'ABC')

# 以Unicode表示的str 通过 encode()方法可以编码为指定的 bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# ERROR 超出编码范围
#print('中文'.encode('ascii'))
#print('中文'.encode('ascii'))
#    ^
#IndentationError: unexpected indent

# decode(),将bytes变为str
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode())
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())

#ERROR 无法解码字节导致报错
#print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
#Traceback (most recent call last):
#  File ".\Exercise\05.str.py", line 32, in #<module>
#    print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
#UnicodeDecodeError: 'utf-8' codec can't #decode byte 0xff in position 3: invalid start byte
# 小部分无效字节，可忽略
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

# str 包含字符长度，len()
print(len('ABC')) #3
print(len('中文')) #2

# len 计算字节数
print(len(b'ABC')) #3
print(len('中文'.encode('utf-8'))) #6

# 占位符测试
print('Hello,%s' % 'Skylar!')
print('整数测试 整数 = %d' % 1122)
print('浮点数测试 数 = %f' % 11.22)
print('Hello everyone!My name is %s,%d years old,from %s.Glade to see you.' % ('Skylar',23,'China'))
print('整数位数测试 整数 = %05d' % 1122)
print('浮点数位数测试 小数 = %.3f' % 11.22)
print('占比达 = %3.2f%%' % 56)

#format()
print('Hello everyone!My name is {0},{1} years old,from {2}.Glade to see you.'.format('Skylar',23,'China'))

# Exercise
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
print('小明去年成绩为%d分,今年成绩提高到%d分,提升比例为：%2.1f%%。' % (72,85,(85-72)/72*100))

