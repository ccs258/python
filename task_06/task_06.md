# 1、函数

在Python中，定义一个函数要使用`def`语句，依次写出函数名、括号、括号中的参数和冒号`:`，然后，在缩进块中编写函数体，函数的返回值用`return`语句返回。以自定义一个求绝对值的`my_abs`函数为例：

```
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
        
        
其调用方式为：my_abs(-99)
```

函数体内部的语句在执行时，一旦执行到`return`时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`。`return None`可以简写为`return`。

# 2、空函数

如果想定义一个什么事也不做的空函数，可以用`pass`语句：

```
def nop():
    pass
```

`pass`语句什么都不做，那有什么用？实际上`pass`可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个`pass`，让代码能运行起来。

`pass`还可以用在其他语句里，比如：

```
if age >= 18:
    pass
```

缺少了`pass`，代码运行就会有语法错误。

# 3、函数参数

## 3.1、位置参数

调用函数时根据函数定义的参数位置来传递参数。例如：

```
def print_hello(name, sex):
    sex_dict = {1: u'先生', 2: u'女士'}
    print 'hello %s %s, welcome to python world!' %(name, sex_dict.get(sex, u'先生'))


# 两个参数的顺序必须一一对应，且少一个参数都不可以
# print_hello('tanggu', 1)
```

## 3.2、关键字参数

用于函数调用，通过“键-值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。

```
# 以下是用关键字参数正确调用函数的实例
# print_hello('tanggu', sex=1)
# print_hello(1, name='tanggu')
# print_hello(name='tanggu', sex=1)
# print_hello(sex=1, name='tanggu')

# 以下是错误的调用方式
# print_hello(name='tanggu', 1)
# print_hello(sex=1, 'tanggu')
```

**可以看出，有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序的**

## 3.3、默认参数

用于定义函数，为参数提供默认值，调用函数时可传可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）

```
# 正确的默认参数定义方式--> 位置参数在前，默认参数在后
def print_hello(name, sex=1):
    ....

# 错误的定义方式
def print_hello(sex=1, name):
    ....

# 调用时不传sex的值，则使用默认值1
# print_hello('tanggu')

# 调用时传入sex的值，并指定为2
# print_hello('tanggu', 2)
```

## 3.4、可变参数

定义函数时，有时候我们不确定调用的时候会传递多少个参数(不传参也可以)。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。

1、包裹位置传递

```
def func(*args):
    ....


# func()
# func(a)
# func(a, b, c)
```

传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是包裹位置传递。

2、包裹关键字传递

```
def func(**kargs):
    ....

# func(a=1)
# func(a=1, b=2, c=3)
```

kargs是一个字典(dict)，收集所有关键字参数；

## 3.5、解包裹参数

*和**，也可以在函数调用的时候使用，称之为解包裹(unpacking)。

1、在传递元组时，让元组的每一个元素对应一个位置参数

```
def print_hello(name, sex):
    print name, sex

# args = ('tanggu', '男')
# print_hello(*args)
# tanggu 男

```

2、在传递词典字典时，让词典的每个键值对作为一个关键字参数传递给函数

```
def print_hello(kargs):
    print kargs

# kargs = {'name': 'tanggu', 'sex', u'男'}
# print_hello(**kargs)
# {'name': 'tanggu', 'sex', u'男'}

```

从上可以看出，python中*args和**kwargs的区别：*args` 表示任何多个无名参数，它是一个tuple；`**kwargs` 表示关键字参数，它是一个dict。

## 3.6、位置参数、默认参数、可变参数的混合使用

基本原则是：先位置参数，默认参数，包裹位置，包裹关键字(定义和调用都应遵循)

```
def func(name, age, sex=1, *args, **kargs):
    print name, age, sex, args, kargs


# func('tanggu', 25, 2, 'music', 'sport', class=2)
# tanggu 25 1 ('music', 'sport') {'class'=2}
```

因此，如果同时使用`*args`和`**kwargs`时，必须`*args`参数列要在`**kwargs`前，像`foo(a=1, b='2', c=3, a', 1, None, )`这样调用的话，会提示语法错误。



# 4、lambda函数

Python中，lambda函数也叫匿名函数，及即没有具体名称的函数，它允许快速定义单行函数，类似于C语言的宏，可以用在任何需要函数的地方。这区别于def定义的函数。

lambda与def的区别：
1）def创建的方法是有名称的，而lambda没有。
2）lambda会返回一个函数对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）。
3）lambda只是一个表达式，而def则是一个语句。
4）lambda表达式” : “后面，只能有一个表达式，def则可以有多个。
5）像if或for或print等语句不能用于lambda中，def可以。
6）lambda一般用来定义简单的函数，而def可以定义复杂的函数。
6）lambda函数不能共享给别的程序调用，def可以。
lambda语法格式：
lambda 变量 : 要执行的语句

```
lambda [arg1 [, agr2,.....argn]] : expression
```

# 7、闭包

- 是函数式编程的一个重要的语法结构，是一种特殊的内嵌函数。

- 如果在一个内部函数里对外层非全局作用域的变量进行引用，那么内部函数就被认为是闭包。

- 通过闭包可以访问外层非全局作用域的变量，这个作用域称为 **闭包作用域**。

- 闭包的返回值通常是函数。

  ```
  def funX(x):
      def funY(y):
          return x * y
  
      return funY
  
  
  i = funX(8)
  print(type(i))  # <class 'function'>
  print(i(5))  # 40
  ```

  

# 8、编写函数的原则

1. 定义函数时，需要确定函数名和参数个数；
2. 如果有必要，可以先对参数的数据类型做检查；
3. 函数体内部可以用`return`随时返回函数结果；
4. 函数执行完毕也没有`return`语句时，自动`return None`；
5. 函数可以同时返回多个值，但其实就是一个tuple；
6. 函数设计要尽量短小，嵌套层次不宜过深；
7. 函数声明应该做到合理、简单、易用；
8. 函数参数设计应该考虑向下兼容；
9. 一个函数只做一件事，尽量保证函数粒度的一致性。

# 9、参考

廖雪峰的官方网站：https://www.liaoxuefeng.com/wiki/1016959663602400/1017106984190464

总结了 90 条写 Python 程序的建议:https://www.ershicimi.com/p/441fbbbbdb8c5eb20bfd4dc9c866beda

Python lambda函数的用法：https://blog.csdn.net/SeeTheWorld518/article/details/46959593