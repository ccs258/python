# 1、字典对象实现原理及特点

**（1）实现原理**

字典的数据结构是散列表，字典是键值对的组合，通过散列表其查询和插入的效率可以达到 O(1)。

字典类型是Python中最常用的数据类型之一，它是一个键值对的集合，字典通过键来索引，关联到相对的值，理论上它的查询复杂度是 O(1)。O(1)是最低的时空复杂度，也即程序运行耗时/耗空间与输入数据大小无关，无论输入数据增大多少倍，耗时/耗空间都不变。 哈希算法就是典型的O(1)时间复杂度，无论数据规模多大，都可以在一次计算后找到目标（不考虑冲突的话）。另外字典是无序的。字典key-value对应示意如下：

![Python——字典dict()详解- C、小明- 博客园](https://img2018.cnblogs.com/blog/1719609/201906/1719609-20190619113938322-608333110.png)

```
>>> d = {'a': 1, 'b': 2}
>>> d['c'] = 3
>>> d
{'a': 1, 'b': 2, 'c': 3}
```

**（2）数据结构特点**

- 字典是一个**无序可变**的数据类型

- **键**不允许重复，**值**无所谓，可作为键：**数值、字符串、元组**，不可作为键：**列表、集合、字典等可变类型**

- 字典在内部维护的**哈希表**使得**检索操作非常快**，非常高效且节约内存

- 字典的插入

  由于字典与集合在插入数据不是每一次都会扩增集合体积，所以会比列表效率高效、省内存空间。虽然会有散列碰撞，但是每次散列碰撞都是二进制数的比较。

  字典中新数据的插入主要取决的数据的散列值和其散列值如何跟其他对象进行比较，其插入过程如下:

  1. 插入数据时，首先计算键的散列值并掩码来得到一个有效的数组索引
  2. 通过索引找到对应的桶(即存储空间)，如果该空间已经被使用，则需要通过一个简单的线性函数计算出新的索引，这一方法称为嗅探
  3. 根据嗅探后获得的新索引找到对应的存储空间，如果空间未被使用，则将键或者键值插入到这一内存块中。

**（3）经典应用—哈希表**

​		哈希表（也叫散列表），根据关键值对(Key-value)而直接进行访问的数据结构。它通过把key和value映射到表中一个位置来访问记录，这种查询速度非常快，更新也快。而这个映射函数叫做哈希函数，存放值的数组叫做哈希表。 哈希函数的实现方式决定了哈希表的搜索效率。具体操作过程是：

1. 数据添加：把key通过哈希函数转换成一个整型数字，然后就将该数字对数组长度进行取余，取余结果就当作数组的下标，将value存储在以该数字为下标的数组空间里。
2. 数据查询：再次使用哈希函数将key转换为对应的数组下标，并定位到数组的位置获取value。

但是，对key进行hash的时候，不同的key可能hash出来的结果是一样的，尤其是数据量增多的时候，这个问题叫做哈希冲突。如果解决这种冲突情况呢？通常的做法有两种，一种是链接法，另一种是开放寻址法，Python选择后者。开放寻址法更多介绍可见：https://ask.hellobi.com/blog/pythoneer/7656。

**（4）拓展-有序字典**

在python中dict对象中的键值对是没有顺序的，但有时候我们需要对字典进行排序，但是在collections模块中有个子类OrderedDict，它能记住字典的插入顺序。

```
>>> d = {2:'b',1:'a',3:'c'}
>>> d
{1: 'a', 2: 'b', 3: 'c'}
>>> d[0]='z'
>>> d
{0: 'z', 1: 'a', 2: 'b', 3: 'c'}
```

标准dict对象添加元素保存在字典中是没有顺序的，从上代码可以看出，但对于OrderedDict就不一样。

```
>>> od = collections.OrderedDict({2:'b',1:'a',3:'c'})
>>> od
OrderedDict([(1, 'a'), (2, 'b'), (3, 'c')])
>>> od[0]='z'
>>> od
OrderedDict([(1, 'a'), (2, 'b'), (3, 'c'), (0, 'z')])
```

od的最后一个项就是最后加入的，很好的按照插入的先后顺序保存在其中。

利用OrderedDict就可以根据自己的需求来自定义排序的规则。

```
>>> # regular unsorted dictionary
>>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

>>> # dictionary sorted by key
>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
```

# 2、集合对象实现原理及特点

**（1）实现原理**

内存的数据结构也是散列表，前面的字典是键值对的组合，而集合就是一堆键的组合存储一组key的数组，里面的key是不重复的。同样通过散列表其查询和插入的效率可以达到 O(1)。

**（2）数据结构特点**

- 集合元素同数学中集合概念一样，有交集、并集、差集等的概念。

- 集合元素是无序可变的、集合里面元素不可重复

- 集合同字典的键一样，数据只能**包含数字、字符串、元组等不可变（可哈希）类型**，不能有可变的类型如**字典、列表、集合等**。‘

  

**（3）经典应用—数据去重、集合推导式**

​		数据去重：在对一批数据进行去重时，不如把这批数据放入集合中。因为在你使用列表存储这批数据时，你需要手动判断是否重复，而且列表会预创建空桶用于存接下来的数据。而集合是一个纯Key的数组，里面的每个数据key时唯一的。

​	    集合推导式：集合推导式的结果是一个集合，可以利用此特点实现想要的效果，优雅便捷。例如：利用集合推导式实现对集合里面元素去除空字串：{s.strip() for s in ('she ', ',', 'i')} 。

​        集合运算：可求交集并集差集、删除操作运算，使用方法如下：

![img](https://img-blog.csdnimg.cn/20181117125314239.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTczNjI4Nw==,size_16,color_FFFFFF,t_70)

# 3、序列对象实现原理及特点

**（1）实现原理**

  序列，指的是一块可存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号（称为索引）访问它们。

序列中，每个元素都有属于自己的编号（索引）。从起始元素开始，索引值从 0 开始递增，如下图 所示。


![img](http://c.biancheng.net/uploads/allimg/190705/2-1ZF5104015S0.gif)

除此之外，Python 还支持索引值是负数，此类索引是从右向左计数，换句话说，从最后一个元素开始计数，从索引值 -1 开始，如下图所示。


![img](http://c.biancheng.net/uploads/allimg/200506/2-2005061011292T.gif)

**（2）数据结构特点**

- 可以通过索引得到每个元素。
- 默认索引值总是从0开始。
- 可以通过分片（例如ls[i:j]切片）的方法得到一个范围内的元素的集合。
- 有很多共同的计算操作符（拼接操作符、运算操作符等）。

**（3）经典应用**--用于遍历

序列应用可列举如下：

有序序列：

- 列表、元组、字符串

无序序列：

- 字典、集合

可变序列：

- 列表、字典、集合

不可变序列：

- 元组、字符串

Python提供一些常用的序列操作的内置函数，如下表所示。

| 函数        | 功能                                                         |
| ----------- | ------------------------------------------------------------ |
| len()       | 计算序列的长度，即返回序列中包含多少个元素。                 |
| max()       | 找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。 |
| min()       | 找出序列中的最小元素。                                       |
| list()      | 将序列转换为列表。                                           |
| str()       | 将序列转换为字符串。                                         |
| sum()       | 计算元素和。                                                 |
| sorted()    | 对元素进行排序。                                             |
| reversed()  | 反向序列中的元素。                                           |
| enumerate() | 将序列组合为一个索引序列，多用在 for 循环中。                |

# 使用场景对比

字典和集合适合于存储能够被索引的数据。当在使用字典和集合处理可以索引的数据时它的时间复杂度是O(1)，但是对于那些不能被索引的数据是徒劳无功的。而序列是一系列数据结构的统称。

而序列包括字符串、列表、元组、集合和字典，序列都支持其上述表格中的通用的操作，但比较特殊的是，集合和字典不支持索引、切片、相加和相乘操作。另外字符串也是一种常见的序列，它也可以直接通过索引访问字符串内的字符。因此，序列适合于同时满足多种不同数据结构的遍历操作。





# 参考

Python 性能优化【2】 -- 高效的使用序列与字典、集合：https://blog.csdn.net/Ahri_J/article/details/77929264

Python字典对象实现原理：https://ask.hellobi.com/blog/pythoneer/7656

《Python高性能编程》——列表、元组、集合、字典特性及创建过程：https://www.bbsmax.com/A/lk5aqe0a51/