# 1、模块

## 1.1、模块的定义与使用

Python中所谓的模块就是一个Python文件，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。模块由代码、函数或类组成。编程中使用模块不仅可以提高代码的可维护性，还可以提高代码可复用性。通过引用模块，每次编程不用都从0开始，引用模块的类型可以是Python内置的模块，也可以是第三方的模块。

模块把一组相关的函数或代码组织到一个文件中，一个文件就是一个模块。模块由代码、函数或类组成。创建一个名为myModule.py的文件，就表示定义了一个名为myModule的模块。假设myModule.py内容如下：

```
def func():
    print "myModule.func()"
    
class MyClass:
    def myFunc(self):
        print "myModule.MyClass.myFunc()"      
```

在myModule模块中定义了一个函数func()和一个类MyClass。我们在myModule.py所在的目录下继续创建一个call_myModule.py的文件。在该文件中调用myModule模块的函数和类。call_myModule.py文件内容如下：

```
import myModule

myModule.func()
myClass = myModule.MyClass()
myClass.myFunc()

输出结果如下：
"""
myModule.func()
myModule.Myclass.myFunc()

"""

```

## 1.2、模块使用注意项

回顾1.1中的模块定义与使用，思考以下几个问题：

1. 调用的call_myModule.py被要求与被调用的myModule模块在一个文件目录下。如果不在一个目录下会有什么问题？如何处理？
2. 导入模块使用import语句。除了import myModule语句，还有其他形式的语句可以用？
3. myModule模块不存在调用func()和MyClass.myFunc()语句。如果存在，调用该模块的程序会出现重复打印吗？如何处理？
4. 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。怎么区分？

上述3个问题，问题（1）与Python模块查找路径有关，问题（2）与模块导入的方法有关，问题（3）与模块的属性有关；分别介绍如下：

（1）python的查找路径

当Python导入一个模块时，Python首先查找当前路径，然后查找lib目录、site-packages目录（安装目录\Lib\site-packages）和环境变量PYTHONPATH设置的目录。简单的说，被调用的模块（包括自定义模块）可以放在和调用程序的文件在同一个层级目录下，或者放在sys.path所列出的目录下。

（2）模块导入的方法

在使用一个模块的函数或类之前，首先要导入模块。模块的导入使用import语句格式如下：

```
import 模块名
```

这条语句可以直接导入一个模块。调用模块的函数或类时，需要以模块名作为前缀，使用格式如下所示：

```
模块名.函数名()
```

如果不想在程序中使用前缀符，可以使用from...import...语句导入，from...import...语句导入主要有3种形式：

（a）导入模块中指定的函数或类

```
from 模块名 import 函数名
```

（b）导入模块中所有的函数和类

```
from myModule import *
```

（c）导入模块中指定的函数和类，并修改为指定名称

```
from myModule import func as myModule_func
```

（3）模块的属性

 模块有一些内置属性，用于完成特定的任务，如__name__、__doc__。每个模块都有一个名称，例如，__name__用于判断当前模块是否是程序的入口，如果当前程序正在被使用，__name__的值为"__main__"。通常给每个模块都添加一个条件语句，用于单独测试该模块功能。

（4）作用域

在模块中，定义函数和变量根据作用域不同可分为以下3种：

- 公开的，可以被直接引用的；例如：`abc`，`x123`，`PI`等；
- 非公开的，类似`_xxx`和`__xxx`这样的函数或变量就是非公开的（private），不应该被直接引用，比如`_abc`，`__abc`等；
- 特殊变量，可以被直接引用用作特殊用途；例如`__author__`，`__name__`就是特殊变量，`hello`模块定义的文档注释也可以用特殊变量`__doc__`访问，我们自己的变量一般不要用这种变量名；

private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量，函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法。总结一下就是：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public，尽量不要取与特殊变量重名的变量名称。

# 2、python时间处理模块

- ### 获取当前日期和时间

  ```
  >>> from datetime import datetime
  >>> now = datetime.now() # 获取当前datetime
  ```

  注意到`datetime`是模块，`datetime`模块还包含一个`datetime`类，通过`from datetime import datetime`导入的才是`datetime`这个类。

  如果仅导入`import datetime`，则必须引用全名`datetime.datetime`。

  `datetime.now()`返回当前日期和时间，其类型是`datetime`。

- ### 获取指定日期和时间

  ```
  >>> from datetime import datetime
  >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
  >>> print(dt)
  2015-04-19 12:20:00
  ```

  要指定某个日期和时间，我们直接用参数构造一个`datetime`：

- ### datetime转换为timestamp

  ```
  >>> from datetime import datetime
  >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
  >>> dt.timestamp() # 把datetime转换为timestamp
  1429417200.0
  ```

  timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）；

- ### timestamp转换为datetime

  ```
  >>> from datetime import datetime
  >>> t = 1429417200.0
  >>> print(datetime.fromtimestamp(t))
  2015-04-19 12:20:00
  ```

  注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。

  本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：

  ```
  2015-04-19 12:20:00
  ```

  实际上就是UTC+8:00时区的时间：

  ```
  2015-04-19 12:20:00 UTC+8:00
  ```

  而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：

  ```
  2015-04-19 04:20:00 UTC+0:00
  ```

  timestamp也可以直接被转换到UTC标准时区的时间：

  ```
  >>> from datetime import datetime
  >>> t = 1429417200.0
  >>> print(datetime.fromtimestamp(t)) # 本地时间
  2015-04-19 12:20:00
  >>> print(datetime.utcfromtimestamp(t)) # UTC时间
  2015-04-19 04:20:00
  ```

- ### str转换为datetime

  ```
  >>> from datetime import datetime
  >>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
  >>> print(cday)
  2015-06-01 18:19:59
  ```

  用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过`datetime.strptime()`实现；注意转换后的datetime是没有时区信息的。

- ### datetime转换为str

```
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now.strftime('%a, %b %d %H:%M'))
Mon, May 05 16:28
```

​	如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过`strftime()`实现的，同样需要一个日期和时间的格式化字符串：

- ### datetime转换为str

  对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用`+`和`-`运算符，不过需要导入`timedelta`这个类：

  ```
  >>> from datetime import datetime, timedelta
  >>> now = datetime.now()
  >>> now
  datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
  >>> now + timedelta(hours=10)
  datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
  >>> now - timedelta(days=1)
  datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
  >>> now + timedelta(days=2, hours=12)
  datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
  ```

  使用`timedelta`可以很容易地算出前几天和后几天的时刻。

# 3、参考

廖雪峰的官方网站：https://www.liaoxuefeng.com/wiki/1016959663602400/1017455068170048

Python入门教程 \] Python模块定义和使用： https://www.cnblogs.com/linyfeng/p/9158339.html

