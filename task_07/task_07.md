# 1、类和对象

![Python 基础08-类和对象- Jamin Zhang](https://jaminzhang.github.io/images/Python/Python-Class-Object.png)

从图可知，一个类通常可以实例化为多个对象，对象与对象之间是独立的；那么类和对象的概念以及特性是怎样的呢？梳理如下:

类：对一类事物的描述，是抽象的、概念上的定义。比如做猫可以作为动物的抽象类；
对象：实际存在的该类事物的每个个体，因而也称实例(instance)。比如不同的猫即为不同的对象；
二者的关系：对象是由类派生的、创建的。一个类可以创建无穷多个对象，每个对象都属于类。

类的特性：每个类有且只有一个`__init__`方法，用于初始化属性。

对象的特性：（1）每一个对象都有自己 独立的内存空间，保存各自不同的属性；（2）多个对象的方法**，**在内存中只有一份，在调用方法时，需要把对象的引用 传递到方法内部。

```
1.创建类，类主要由类名，属性，方法组成,当然创建一个类时，属性和方法可以选择的。
class Person:
    def cry(self):  #类方法：跟函数的定义类似，但是self参数自带的，这也是类的方法和普通方法的区别。
        print("I can cry")
    def speak(self):
        print("I can speak:%s"%(self.word))
 
---------创建对象----------------------------------------------------------------------
tom =Person()  #创建对象，直接类名(),不用像java中还要new，所以python更加简洁
tom.cry()     #调用对象的方法
tom.word="hahah"
tom.speak()
tom.age =18  #给对象添加属性 ，属性不用在类定义时声明，但这种方法给对象赋值麻烦，每个对象都要赋值。
tom.age =19  #上面已经给tom添加过age属性，再次属于调用，重新赋值。
 
----------执行结果---------------------------------------------------------------------
'''
I can cry
I can speak:hahah
'''
 
2._init_(self)方法实现类初始化属性，有点类似java中类的构造器。
-------------------------------------------------------------------------------------
class Person1:
    def __init__(self):  #_init_(self),主要给类初始化一些属性，对象创建时自动调用该方法执行
        self.country ="china"
        self.sex = "male"
 
    def speak(self):
        print("I am  from %s  ,wuwuwuwuu"%self.country)
-------------创建对象------------------------------------------------------------------
jack = Person1()
jack.speak()
print(jack.country,jack.sex)
 
tom=Person1()
tom.speak()
print(tom.country,tom.sex)
--------------执行结果如下：------------------------------------------------------------
'''
I am  from china  ,wuwuwuwuu
china male
I am  from china  ,wuwuwuwuu
china male
'''
对于__init__()方法,还有以下几点需要注意的:
（1）、__init__()方法，在创建一个对象时默认被调用，类似Java中构造器。不需要手动调用
（2）、__init__(self)中，默认有1个参数名字为self，必须写。如果在创建对象时传递了2个实参，__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,age,name).第一个self不需要手动传参。 
（3）、__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
python中一个类中只能有一个__init__方法，不支持该方法的重载（类似java中构造器的重载）


3.可以通过初始化时调用参数的形式,给每个对象赋不同的属性值
 
class Person2:
    def __init__(self,name,age): 
        self.age =age   #这种用法类似java中的this.age=age.self意思可以理解为当前对象
        self.name = name #表示将当前对象传进来的参数name的值赋给当前对象的属性name
        self.country = "china" #还是可以给类的每个对象都赋一个默认值。
 
    def speak(self):
        print("name=%s,age=%d"%(self.name,self.age))
-----------创建对象--------------------------------------------------------------------
p1 = Person2("allen",19)
p2 = Person2("sherry",22)
p3 = p2  #让p3=p2.对象的赋值
 
p1.speak()
p2.speak()
 
print("p1：",p1)  #直接打印对象 ，打印的是对象在内存中地址。
print("p2:",p2)
print("p3:",p3) #发现p3的地址跟p2的地址一样。
 
'''执行结果如下：
name=allen,age=19
name=sherry,age=22
p1： <__main__.Person2 object at 0x000001CBA3508BE0>
p2: <__main__.Person2 object at 0x000001CBA3508CF8>
p3: <__main__.Person2 object at 0x000001CBA3508CF8>

```

# 2、新式类与经典类

Python 有[两种类](http://wiki.python.org/moin/NewClassVsClassicClass)：经典类（classic class）和新式类（new-style class）。两者的不同之处在于新式类继承自 `object`。在 Python 2.1 以前，经典类是唯一可用的形式；Python 2.2 引入了新式类，使得类和内置类型更加统一；在 Python 3 中，新式类是唯一支持的类。总结梳理如下：

- **新式类**：以 `object` 为基类的类，**推荐使用**

- **经典类**：不以 `object` 为基类的类，**不推荐使用**

- 在 `Python 2.x` 中定义类时，如果没有指定父类，则不会以 `object` 作为 **基类**

- 在 `Python 3.x` 中定义类时，如果没有指定父类，会 **默认使用** `object` 作为该类的 **基类** —— `Python 3.x` 中定义的类都是 **新式类**

  特别注意：新式类 和 经典类 在多继承时 —— 会影响到方法的搜索顺序；为了保证编写的代码能够同时在 `Python 2.x` 和 `Python 3.x` 运行！在定义类时，**如果没有父类，建议统一继承自 `object。`**

  ```
  class 类名(object):    
      pass
   
  #尽量不要用下面这种老是写法，虽然不会报错，但是不推荐
  class 类名: 
  
  ```

# 3、多继承时方法的搜索顺序

对于支持继承的编程语言来说，其方法（属性）可能定义在当前类，也可能来自于基类，所以在方法调用时就需要对当前类和基类进行搜索以确定方法所在的位置。举例如下：



![img](https://img-blog.csdn.net/20170830113338026?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMTAxOTcyNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

```
class A:
    def say(self):
        print("A Hello:", self)

class B(A):
    def eat(self):
        print("B Eating:", self)

class C(A):
    def eat(self):
        print("C Eating:", self)

class D(B, C):
    def say(self):
        super().say()
        print("D Hello:", self)
    def dinner(self):
        self.say()
        super().say()
        self.eat()
        super().eat()
        C.eat(self)

if __name__ == '__main__':
    dd = D()
    print(dd.dinner())
    import inspect  #利用该包查看下调用顺序
    print(inspect.getmro(D))

"""
结果是：
A Hello: <__main__.D object at 0x000002175067B978>
D Hello: <__main__.D object at 0x000002175067B978>
A Hello: <__main__.D object at 0x000002175067B978>
B Eating: <__main__.D object at 0x000002175067B978>
B Eating: <__main__.D object at 0x000002175067B978>
C Eating: <__main__.D object at 0x000002175067B978>
None #默认没有返回值；
第一个self.say()，运行A类的say()再print出自己的第二行信息
第二个super().say()，运行A类的say()
第三个self.eat()，根据 __mro__ ， 找到的是 B 类实现的eat方法
第四个super().eat()，根据 __mro__ ， 找到的是 B 类实现的eat方法
第五个C.eat(self)忽略 __mro__ ， 找到的是 C 类实现的eat方法

(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)  #可以看出子类D的继承顺序为：D->B->C->A

"""
```

当单继承存在时，调用方法的大体策略：
（1）self.method()默认会调用当前类的method()方法；
（2）super().method()会调用当前类父类的method()方法；

但如果当前类的父类有多个，即为多继承时，python默认是按照`__mro__`去调用的；

![菱形继承](https://hanjianwei.com/2013/07/25/python-mro/class_diamond.svg)

针对python2的经典继承，python2采用了简单的MRO方法：从左至右的[深度优先遍历](http://en.wikipedia.org/wiki/Depth-first_search)。上述「菱形继承」为例，其查找顺序为 `[D, B, A, C, A]`，如果只保留重复类的第一个则结果为 `[D, B, A, C]`。代码测试验证如下：

```
>>> import inspect
>>> class A:
...     def show(self):
...         print "A.show()"
...
>>> class B(A): pass
>>> class C(A):
...     def show(self):
...         print "C.show()"
...
>>> class D(B, C): pass
>>> inspect.getmro(D)
(<class __main__.D at 0x105f0a6d0>, <class __main__.B at 0x105f0a600>, <class __main__.A at 0x105f0a668>, <class __main__.C at 0x105f0a738>)
```

而按照新式类继承，MRO方法则会采用深度遍历，同样以上述「菱形继承」为例，其查找顺序为 `[D, B, A, object, C, A, object]`，重复类只保留最后一个，因此变为 `[D, B, C, A, object]`。代码测试验证如下：

```
>>> class A(object):
...     def show(self):
...         print "A.show()"
...
>>> class B(A): pass
>>> class C(A):
...     def show(self):
...         print "C.show()"
...
>>> class D(B, C): pass
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
```

当类是经典类时：多继承状态下，按深度优先查找。

当类是新式类时：多继承状态下，按广度优先查找。

广度优先的顺序：走一步不走到头，而是先把旁边同层的都走完，才开始按此策略再走剩下的分支。

深度优先的顺序：一走就走到头，走完再回溯后按此策略走剩下的分支；

![Python之面向对象新式类和经典类- osc_tm2zceka的个人空间- OSCHINA](https://oscimg.oschina.net/oscnet/f5adab6db475f73204378f6bb2de4a3679e.png)

另注意：我们知道当实例化了一个对象之后，dd = D()，其本身类和父类（也包括父类的父类）里面方法的self对象代表的都是当前类本身，而不是父类的对象，而是我们实例化对象；理解这个概念：实例化之后就只会有当前实例化的一个对象，继承的关系只是表明当前类具有父类里面的那些方法，相当于省略了重写这个方法的过程，但self还是最上层的那个实例化的对象。

#4、魔法方法

**（1）、什么是Python魔法方法?**

魔法方法就如同它的名字一样神奇，总能在你需要的时候为你提供某种方法来让你的想法实现。魔法方法是指Python内部已经包含的，被双下划线所包围的方法，这些方法在进行特定的操作时会自动被调用，它们是Python面向对象下智慧的结晶。初学者掌握Python的魔法方法也就变得尤为重要了。

**（2）、为什么要使用Python魔法方法?**

使用Python的魔法方法可以使Python的自由度变得更高，当不需要重写时魔法方法也可以在规定的默认情况下生效，在需要重写时也可以让使用者根据自己的需求来重写部分方法来达到自己的期待。而且众所周知Python是支持面向对象的语言Python的基本魔法方法就使得Python在面对对象方面做得更好。

**（3）、基础魔法方法（较为常用）**

**__new__(cls[, ...])** 才是实例化对象调用的第一个方法，它只取下 cls 参数，并把其他参数传给 __init__。 __new__很少使用，但是也有它适合的场景(单例模式)，尤其是当类继承自一个像元组或者字符串这样不经常改变的类型的时候。

**__init__(self[, ...])**构造方法，初始化类的时候被调用

**__del__(self)**析构方法，当实例化对象被彻底销毁时被调用（实例化对象的所有指针都被销毁时被调用）

**__call__(self[, args...])**允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)

**__len__(self)**定义当被 len() 调用时的行为__repr__(self)定义当被 repr() 调用时的行为

**__str__(self)**定义当被 str() 调用时的行为__bytes__(self)定义当被 bytes() 调用时的行为

**__hash__(self)**定义当被 hash() 调用时的行为

**__bool__(self)**定义当被 bool() 调用时的行为，应该返回 True 或 False

**__format__(self, format_spec)**定义当被 format() 调用时的行为

**（4）、属性相关的方法**

**__getattr__(self, name)**定义当用户试图获取一个不存在的属性时的行为

**__getattribute__(self, name)**定义当该类的属性被访问时的行为

**__setattr__(self, name, value)**定义当一个属性被设置时的行为

**__delattr__(self, name)**定义当一个属性被删除时的行为

**__dir__(self)**定义当 dir() 被调用时的行为

**__get__(self, instance, owner)**定义当描述符的值被取得时的行为

**__set__(self, instance, value)**定义当描述符的值被改变时的行为

**__delete__(self, instance)**定义当描述符的值被删除时的行为

**（5）、比较操作符**

__lt__(self, other)定义小于号的行为：x < y 调用 x.__lt__(y)

__le__(self, other)定义小于等于号的行为：x <= y 调用 x.__le__(y)

__eq__(self, other)定义等于号的行为：x == y 调用 x.__eq__(y)

__ne__(self, other)定义不等号的行为：x != y 调用 x.__ne__(y)

__gt__(self, other)定义大于号的行为：x > y 调用 x.__gt__(y)

__ge__(self, other)定义大于等于号的行为：x >= y 调用 x.__ge__(y)

**（6）、类型转换**

__complex__(self)定义当被 complex() 调用时的行为（需要返回恰当的值）

__int__(self)定义当被 int() 调用时的行为（需要返回恰当的值）

__float__(self)定义当被 float() 调用时的行为（需要返回恰当的值）__round__(self[, n])定义当被 round() 调用时的行为（需要返回恰当的值）

**（7）、容器类型（一般用于操作容器类）**

__len__(self)定义当被 len() 调用时的行为（一般返回容器类的长度）

__getitem__(self, key)定义获取容器中指定元素的行为，相当于 self[key]

__setitem__(self, key, value)定义设置容器中指定元素的行为，相当于 self[key] = value

__delitem__(self, key)定义删除容器中指定元素的行为，相当于 del self[key]

__iter__(self)定义当迭代容器中的元素的行为

__reversed__(self)定义当被 reversed() 调用时的行为

__contains__(self, item)定义当使用成员测试运算符（in 或 not in）时的行为

# 5、参考

Python中的类的定义和对象的创建：https://blog.csdn.net/qq_26442553/article/details/81744890

python 多重继承的方法解析顺序：https://blog.csdn.net/u011019726/article/details/77712080

Python的方法解析顺序(MRO)：https://hanjianwei.com/2013/07/25/python-mro/

python 的魔法方法是什么?：https://zhuanlan.zhihu.com/p/38347855