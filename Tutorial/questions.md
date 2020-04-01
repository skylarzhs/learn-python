### 学习中的问题

先记录，查询，不理解内容，在后续章节中找答案，学习完成一遍之后重新来看问题。

1. 函数加载问题

    在命令行使用`import`加载函数，在目录下生成`__pycache__`文件夹`quadratic.cpython-38.pyc`文件。
    文件改动不会自动加载修改后的文件，需要退出命令行重新进入后才会重新加载。
    网上查的资源都是进行模块加载，应用于函数不起作用，`reload() argument must be a module`。

2. `input()`输入问题

    `input()`函数输出为字符串，如何优雅的将字符串转化成数字类型。兼容整数与浮点数。

3. 参数章节中的问题

    再利用`tuple`与`dict`传参的时候，`*`和`**`的区别是什么？两个分别进行了怎样的数据操作？

    实际试验中对关键字参数取`*`，取出的为键名组进`tuple`中作为可变参数。

```
def f1(a, b, c=0, *args, **kw):
    print(a, b, c, args, kw)

args = (1, 2, 3, 4)

kw = {'kw1': 1122, 'kw2': 990}

f1(*args, **kw) # 常规调用
# 1 2 3 (4,) {'kw1': 1122, 'kw2': 990}

f1(*args, *kw) #单个*取键名作为可变参数的一部分
# 1 2 3 (4, 'kw1', 'kw2') {}
```

4. 生成器

    生成器中关于`yield`的概念理解不是很清楚。

5. 奇怪的案例

```
>>> try:
...     print('try...')
...     r = 10 / 0
...     print('result:',r)
... except ZeroDivisionError as e:
...     print('except:',e)
... finally:
...     print('finally...')
...
try...
except: division by zero
finally...
>>> try:
...     print('try...')
...     r = 10 /0
...     print('result:',r)
... except ZeroDivisionError as e:
...     print('except:',e)
... finally:
...     print('finally...')
... print('end')
  File "<stdin>", line 9
    print('end') ###############运行出错，原因？？
    ^
SyntaxError: invalid syntax
```