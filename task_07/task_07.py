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
    # print(dd.dinner())
    import inspect
    print(inspect.getmro(D))
"""
结果是：
A Hello:object_A
D Hello:object_D
A Hello:object_A
B Eating:object_B  #或者 C Eating:object_C
B Eating:object_B  #或者 C Eating:object_C
C Eating:object_C

当多继承存在时，调用方法的策略：
（1）self.method()默认会调用当前类的method()方法；
（2）super().method()会调用当前类父类的method()方法；如果当前类的父类有多个，
默认是按照传入继承父类的顺序去调用的，从左至右，调用实现；



"""