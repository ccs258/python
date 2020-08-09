# 1、python的file对象与open函数

file对象是Python内置的数据类型，通过Python内置的open()函数打开文件可以获得一个file对象。

## **1.1、 open()函数**

　　open()函数的格式如下：

```
open``(filename, mode``=``'r'``, bufsize``=``-``1``)
```

　　open()返回一个file对象，它是Python内置的file类型的一个实例。

　　open()函数各个参数的含义如下：

- filename：格式：字符串。含义：要打开的文件的路径，可以绝对路径，也可以是相对路径。注意，**在Unix和Windows上，都可以使用斜杠“/”作为目录的分隔符**。在Windows中，路径分隔符是反斜杠“\”，这与正则表达式中的转义符号相同，因此**windows文件路径中需要使用"\\"表示目录**，如：'c:\\test\\test.txt'，或使用Python中的raw string，如 r'c:\test\test.txt'，来表示路径，Linux中则无此要求。
- mode：格式：字符串。含义：以哪种读写模式打开文件。mode的可选项见下文。
- bufsize：格式：整型。含义：为文件设置的缓存。bufsize=0时，等价于unbuffer形式，写到文件的内容立即被刷到硬盘；bufsize=1时，表示行缓冲，每一次写入"\n"后，内容就被刷到硬盘。bufsize < 0时，使用系统默认的缓冲大小；bufsize > 1时，使用其作为文件的缓冲大小。

##  1.2、参数mode的取值与含义

　　'r' —— 只读模式，**要求目标文件必须存在。**

　　'w' —— 只写模式，**如果目标文件已存在，将会截断目标文件并覆盖其内容**；如果目标文件不存在，则新建之。

　　'a' —— 追加模式，只写打开目标文件，如果目标文件已存在，写入的内容追加到源文件的结尾；如果目标文件不存在，则创建之。

　　'r+' —— 读写模式，**要求目标文件必须存在，此时写入，并不会截断源文件，而是替换源文件中相应位置的内容。**

　　'w+' —— 读写模式，**如果目标文件已存在，将会截断目标文件并覆盖其内容**；如果目标文件不存在，则新建之。

　　'a+' —— 追加模式，读写打开目标文件，如果目标文件已存在，写入的内容追加到源文件的结尾；如果目标文件不存在，则创建之。

## 1.3、file对象的属性、方法

| f.closed               | 只读属性，判断f.close()是否已经调用过。                      |
| ---------------------- | ------------------------------------------------------------ |
| f.encoding             | 只读属性，文件的encoding格式                                 |
| f.mode                 | 只读属性，显示调用open()打开文件时指定的mode                 |
| f.name                 | 只读属性，显示调用open()文件时的指定名称                     |
| f.newlines             |                                                              |
| f.softspace            | 只读的布尔属性，供print语句记录自己的状态，file对象自身并不修改或使用该属性。 |
| f.errors               |                                                              |
| f.close()              | 关闭已经打开的file对象，所有的file对象，完成读写操作后，都应该关闭 |
| f.flush()              | 手动将Python写到文件的缓存刷到操作系统                       |
| f.isatty()             | 如果 f 是一个交互终端，则返回True，否则，返回False           |
| f.fileno()             | 返回一个整数，这个整数就是文件 f 的文件描述字——file descriptor，fd。 |
| f.read(size = -1)      | 读取文件内容，以字符串的形式返回。size < 0 —— 一直读到文件结尾；size > 0 —— 读取 size 字节的内容直到文件结尾，如果到了文件末尾仍未满 size 字节，则返回全文。size = 0 —— size = 0 或读取时当前文件的位置在文末，都会返回一个空字符串。 |
| f.readline(size = -1)  | 读取1行，直到遇见'\n'或读满size字节，以字符串的形式返回。size >= 0，读取的内容不超过size字节，如果没有读够 size 字节就到本行结尾，则停止读取，返回本行。size < 0，读取当前一行的全部内容，直到遇到 '\n' 或文件结尾。 |
| f.readlines(size = -1) | 读取多行，返回一个list，每一行作为 list 中的一个字符串。最后一个字符串可能不以 “ \n ”结尾。 |
| f.next()               | file对象是可迭代的，每次迭代返回文件中的一行。               |
| f.seek(pos, how = 0)   | 将当前文件的位置设置到距离参考点pos字节的位置，参数 how 决定参照点的位置：how = 0，参照点是文件开头，这是默认情形，对应于 os.SEEK_SEThow = 1，参考点是当前位置，对应于os.SEEK_CURhow = 2，参考点是文末，对应于os.SEEK_END |
| f.tell()               | 返回文件当前位置距离文件开头的字节数。                       |
| f.truncate([size])     | 将文件截断到不超过 size 字节，如果size超过当前文件大小，将以0填充，如果没有提供size参数，则使用 f.tell() 作为截断后新文件的大小。 |
| f.write(s)             | 将字符串 s 写入到文件中                                      |
| f.writelines(lst)      | 参数lst是一个**可迭代对象**，将其中的字符串内容全部写到 f 中，该函数不会自动添加 '\n' ！ |

## 1.4、可迭代的file对象

file对象是可迭代的，

```
for line  in f:
	...
```

会依次遍历 f 中的每一行。

##  1.5、with open打开文件

常规的打开文件的方式如下：

```

file = open("test.txt","r")
for line in file.readlines():
    print line
file.close()
```

如读取过程中文件不存在或异常，则直接出现错误，close方法无法执行，文件无法关闭；因此，可以采用with语句解决此问题。

```
with open("test.txt","r") as file:
for line in file.readlines():
    print line
```

用with语句的好处，就是到达语句末尾时，会自动关闭文件，即便出现异常。

with语句实际上是一个非常通用的结构，允许你使用所谓的上下文管理器。上下文管理器是支持两个方法的对象：__enter__和__exit__。

方法__enter__不接受任何参数，在进入with语句时被调用，其返回值被赋给关键字as后面的变量。

方法__exit__接受三个参数：异常类型、异常对象和异常跟踪。它在离开方法时被调用（通过前述参数将引发的异常提供给它）。如果__exit__返回False，将抑制所有的异常。

文件也可用作上下文管理器。它们的方法__enter__返回文件对象本身，而方法__exit__关闭文件

```python
file= open("test.txt","r")
try:
    for line in file.readlines():
        print line
except:
    print "error"
finally:
	file.close()
```

with语句作用效果相当于上面的try-except-finally。

# 2、python的OS模块

python中OS模块常用的函数如下：

- `os.sep`:取代操作系统特定的路径分隔符
- `os.name`:指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
- `os.getcwd`:得到当前工作目录，即当前python脚本工作的目录路径。
- `os.getenv()`和`os.putenv`:分别用来读取和设置环境变量
- `os.listdir()`:返回指定目录下的所有文件和目录名
- `os.remove(file)`:删除一个文件
- `os.stat（file）`:获得文件属性
- `os.chmod(file)`:修改文件权限和时间戳
- `os.mkdir(name):`创建目录
- `os.rmdir(name)`:删除目录
- `os.removedirs（r“c：\python”）`:删除多个目录
- `os.system()`:运行shell命令
- `os.exit()`:终止当前进程
- `os.linesep`:给出当前平台的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
- `os.path.split()`:返回一个路径的目录名和文件名
- `os.path.isfile()`和`os.path.isdir()`分别检验给出的路径是一个目录还是文件
- `os.path.existe()`:检验给出的路径是否真的存在
- `os.listdir(dirname)`:列出dirname下的目录和文件
- `os.getcwd()`:获得当前工作目录
- `os.curdir`:返回当前目录（'.'）
- `os.chdir(dirname)`:改变工作目录到dirname
- `os.path.isdir(name)`:判断name是不是目录，不是目录就返回false
- `os.path.isfile(name)`:判断name这个文件是否存在，不存在返回false
- `os.path.exists(name)`:判断是否存在文件或目录name
- `os.path.getsize(name)`:或得文件大小，如果name是目录返回0L
- `os.path.abspath(name)`:获得绝对路径
- `os.path.isabs()`:判断是否为绝对路径
- `os.path.normpath(path)`:规范path字符串形式
- `os.path.split(name)`:分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
- `os.path.splitext()`:分离文件名和扩展名
- `os.path.join(path,name)`:连接目录与文件名或目录
- `os.path.basename(path)`:返回文件名
- `os.path.dirname(path)`:返回文件路径

# 3、参考

open()和with open() as的区别：https://blog.csdn.net/a1496785/article/details/83011974

（原创）Python文件与文件系统系列（1）—— file 对象：https://www.cnblogs.com/Security-Darren/p/4728395.html

python之OS模块详解：https://www.cnblogs.com/cherishry/p/5725977.html

