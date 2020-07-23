# 1、条件语句

任何编程语言都提供了 if...else... 语句，表示如果（if）满足条件就做某件事，否则（else）就做另外一件事。根据具体情况的不同，条件语句有以下几种变种；

## 1.1 if语句

```
if expression:
    do A
核心点：只关注某个情况发生要做的事，表达1种情况；
翻译为通俗语言就是：如果某个情况发生，就做某事；

```

## 1.2 if...else...语句

```
if expression:
    do A
else:
    do B 
核心点：关注某个情况发生或未发生分别要做的事，表达2种情况；
翻译为通俗语言就是：如果某个情况发生，就做A事；否则，就做B事

```

## 1.3 if...elif...else...语句

```
if expression1:
    do A
elif expression2:
	do B:
else:
    do C 
    
核心点：关注某个情况有多种时，分别对应要做的事，表达3种及以上情况；
翻译为通俗语言就是：如果情况1发生，就做A事；如果情况2发生，就做B事；否则，就做C事

```

## 1.4 assert 关键词

Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。

![img](https://www.runoob.com/wp-content/uploads/2019/07/assert.png)

语法格式如下：

```
assert expression
```

等价于：

```
if not expression:
    raise AssertionError
```

assert 后面也可以紧跟参数:

```
assert expression [, arguments]
```

等价于：

```
if not expression:
    raise AssertionError(arguments)
```

# 2 循环语句

上一节中，我们知道某个条件为真则执行相应代码块的if语句，实际上，我们还会遇到一些情况，当某个条件为真，则一直执行某项操作，直到条件为假；等看起来很复杂情况。实际上，计算机擅长处理人类觉着重复枯燥的事情。下面将探索循环，感受计算机处理特定重复事情的简洁与优雅。

## 2.1 for循环

for 循环用于**迭代**容器对象中的元素，这些对象可以是**列表、元组、字典、集合、文件**，甚至可以是自定义类或者函数。for循环本质就是不断地调用迭代器的`__next__`方法，直到有StopIteration为止，所以任何可迭代对象都可以作用在for循环中。

for循环底层的循环步骤：

1. 先判断对象是否为可迭代对象，不是的话直接报错，抛出TypeError异常，是的话，调用 `__iter__`方法，返回一个迭代器
2. 不断地调用迭代器的`__next__`方法，每次按序返回迭代器中的一个值
3. 迭代到最后，没有更多元素了，就抛出异常 StopIteration，这个异常 python 自己会处理，不会暴露给开发者

## 2.2 while循环

通常while条件里面的变量需要单独的初始化，相比for循环而言，某些只做序列遍历直接处理，for循环更为通用和简洁。

## 2.3 循环结束之continue和break

```text
continue语句会中断本轮循环、开始新迭代（进入“下一轮”代码块执行流程）；
break会直接结束循环。

```

## 2.4 循环中的else语句

通常，在循环中使用break是“发现”了什么或“出现”了什么情况。要在循环提前结束时采取某种措施很容易，但有时候可能想在**循环正常结束**时才采取某种措施。如何**判断循环是提前结束还是正常结束的**呢？一种简单的办法是在循环中添加一条else子句，它仅在没有调用break时才执行。

```text
sum = 0
for i in range(1,60):
    sum = sum + i
    if sum == 1200:
        print(i)
        break
else:
    print("Didn't find it!")
此处的else语句就能起到判断循环的结束是否是异常触发了break导致的还是自然结束的；
```



## 2.3 使用建议

无论是在for循环还是while循环中，都可使用continue、 break和else子句。

建议只要能够使用for循环，就不要使用*while循环*。

# 3 知识点扩展

## 3.1 python中的迭代器、可迭代对象、生成器

通过上节知道，for 循环是对容器进行迭代的过程，什么是迭代？迭代就是从某个容器对象中逐个地读取元素，直到容器中没有更多元素为止。

`class MyRange:`
`...     def __init__(self, num):`
`...         self.num = num`
`...`
`for i in MyRange(10):`
`...     print(i)`
`...`
`Traceback (most recent call last):`
`File "<stdin>", line 1, in <module>`
`TypeError: 'MyRange' object is not iterable`

MyRange 不是一个可迭代对象，所以它不能用于迭代，那么到底什么样的对象才称得上是可迭代对象(iterable)呢？

可迭代对象需要实现`__iter__`方法，并返回一个迭代器，什么是迭代器呢？迭代器只需要实现 `__next__`方法。现在我们就来验证一下列表为什么支持迭代：

​                        

```
>>> x = [1,2,3]
>>> its = x.__iter__() # x有此方法，说明列表是可迭代对象
>>> its
<list_iterator object at 0x100f32198>

>>> its.__next__()  # its有此方法，说明its是迭代器
1
>>> its.__next__()
2
>>> its.__next__()
3
>>> its.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

# 4 作业解答

1、编写一个Python程序来查找那些既可以被7整除又可以被5整除的数字，介于1500和2700之间。

```
`rst = []`

`for i in range(1500,2701):`

​	 `if i % (5*7) == 0:`

​			 `rst .append(i)`
```

2、龟兔赛跑游戏

```python
v1, v2, t, s, l = map(int, input().split()) #输入兔子的速度v1（表示每秒兔子能跑v1 米），乌龟的速度v2，以及兔子对应的t，s值（任一秒结束后兔子发现自己领先t米或以 上，它们就会停下来休息s秒），以及赛道的长度l——就能预测出比赛的结果。
time, s1, s2 = 0, 0, 0  #s1表示兔子跑的距离，s2表示乌龟跑的距离，time表示兔子休息的时间；
while s2 < l and s1 < l:  #兔子及乌龟跑的距离都要小于总长度l;
    s1 += v1    #兔子正常的跑
    s2 += v2 #乌龟正常的跑
    time += 1 #正常的计时
    if s1 >= l or s2 >= l:   #兔子或乌龟跑的距离任一一个大于总长度l，则为胜方，比赛结束
        break
    if s1 - s2 >= t:  #兔子发现自己领先t米或以 上，它们就会停下来休息s秒
        s1 -= s * v1
if s1 == s2: #兔子或乌龟同时到达，平局
    print("D")
elif s1 > s2:#兔子先到，兔子胜
    print("R")
else:#否则（只剩下一种情况：乌龟先到），乌龟胜
    print("T")
print(time)

思路：见上述代码注释！

```

# 5 参考

耐人寻味的 for...else...语句：https://foofish.net/for-else.html

Python3 assert（断言）：https://www.runoob.com/python3/python3-assert.html

python中for循环的工作原理：https://segmentfault.com/a/1190000010219463

Python3 assert（断言）：https://www.runoob.com/python3/python3-assert.html

耐人寻味的 for...else...语句：https://foofish.net/for-else.html

3.3 循环：https://zhuanlan.zhihu.com/p/107088358

