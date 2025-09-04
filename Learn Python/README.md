## Important Questions and Answer of Python

**১. Python কীভাবে কাজ করে (.py থেকে output পর্যন্ত)?**

Python হল interpreted language। যখন আপনি .py ফাইল রান করেন:
- Python Interpreter প্রথমে .py ফাইলকে source code হিসেবে পড়ে।
- Source code কে Python bytecode এ কম্পাইল করে (.pyc ফাইলে সংরক্ষণ করতে পারে)।
- Bytecode Python Virtual Machine (PVM) দ্বারা execute হয়।
- VM step-by-step bytecode execute করে এবং আপনাকে desired output প্রদান করে।
> সারসংক্ষেপ: .py → bytecode → PVM → output

**২. type নিজেই class এবং সব class এর metaclass type হলে Python কিভাবে circular dependency handle করে?**

- Python এ circular dependency আসলেও সমস্যা হতো, যদি interpreter একে সাধারণ নিয়মে তৈরি করত।
- কিন্তু C level এ special bootstrapping এর মাধ্যমে type আর object কে তৈরি করে।
- পরে self-referential linking করা হয় → type.__class__ = type।
- ফলে Python এ সব class type এর instance হতে পারে, আর type নিজেই নিজের class হয়।
> C level bootstrapping মানে হলো Python এর সবচেয়ে বেসিক class (যেমন object, type) কে C ভাষায় manually বানানো, যাতে Python interpreter নিজেকে initialize করতে পারে।

**৩. Python এ GIL (Global Interpreter Lock) এর প্রয়োজন কেন?**

- Python এর CPython implementation memory safety এবং thread safety নিশ্চিত করতে GIL ব্যবহার করে।
- একসাথে একাধিক thread কে Python bytecode execute করতে না দেয়।
- ফলে C extension modules ছাড়া multithreading এ race condition কমে।
- drawback: CPU-bound tasks এ একাধিক core ব্যবহার করতে পারে না।

> Interpreter হলো এমন একটা প্রোগ্রাম, যেটা কোডকে line-by-line পড়ে এবং সাথে সাথে চালায়। Python interpreter (CPython) bytecode তৈরি করে, তারপর PVM দিয়ে সেটাকে চালায়।

> Compiler বনাম Interpreter:
> - Compiler: পুরো কোড একসাথে machine code এ রূপান্তর করে, তারপর চালায়। (C, C++)
> - Interpreter: কোড লাইন-বাই-লাইন চালায়, সাথে সাথে output দেয়। (Python, JavaScript)

**৪. Python এ memory management কিভাবে হয়?**

- সবকিছু object আর object গুলো heap memory তে store হয়।
- Reference counting দিয়ে ট্র্যাক করা হয়, কে কতবার ওই object ব্যবহার করছে।
- যদি reference count = 0 হয় object মেমরি থেকে মুছে যায়।
- Garbage Collector (GC) extra কাজ করে, circular reference গুলোও মুছে দেয়।
- PyMalloc allocator ছোট object এর জন্য efficient memory block manage করে।
> সংক্ষেপে: Python এ memory নিজে ম্যানেজ করতে হয় না; interpreter automatically reference counting + garbage collection দিয়ে manage করে।

**৫. Pass by value এবং pass by reference (data type অনুযায়ী)**

- Python সবকিছু object reference দ্বারা pass করে।
- Immutable types (int, str, tuple): behave like pass-by-value।
- Mutable types (list, dict, set): behave like pass-by-reference।
```python
def f(x):
    x += 1  # Immutable → নতুন object তৈরি হয়

def g(lst):
    lst.append(4)  # Mutable → original object modify হয়
```

**৬. Custom Iterator, Context Manager, Generator, Decorator**

**Custom Iterator**

Iterator মানে হলো object যেটা একটার পর একটা value return করতে পারে (`__iter__`, `__next__`) ব্যবহার করে।

```python
class Count:
    def __init__(self, n):
        self.n, self.i = n, 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        raise StopIteration

for x in Count(3):
    print(x)   # 1, 2, 3
```
**Context Manager**

Context Manager with statement দিয়ে resource handle করতে সাহায্য করে (`__enter__`, `__exit__`)।

```python
class MyFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFile("test.txt") as f:
    f.write("Hello")
```
**Generator**

Generator হলো এমন function যেটা yield ব্যবহার করে একটার পর একটা value produce করে।

```python
def gen(n):
    for i in range(n):
        yield i

for x in gen(3):
    print(x)   # 0, 1, 2
```
**Decorator**

Decorator হলো function যেটা অন্য function কে modify বা extend করে।

```python
def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@deco
def hello():
    print("Hello")

hello()
# Before → Hello → After
```

**৭. `__name__` == "`__main__`" এর মানে?**

- যখন Python script directly run হয়, `__name__` = "`__main__`" হয়।
- অন্য script থেকে import করলে `__name__` হবে module name।
- এটা ব্যবহার করে main code block শুধুমাত্র direct execution এর জন্য run করা যায়।

**৮. Python এর Scopes**

Python এ variable খোঁজার সময় একটা নির্দিষ্ট order follow করে, যেটাকে বলে LEGB Rule।

**🔹 Local (L)**

Function এর ভিতরে declare করা variable।
```python
def func():
    x = 10  # Local
    print(x)
```
**🔹 Enclosing (E)**

Nested function এর outer function এর variable।
```python
def outer():
    y = 20  # Enclosing
    def inner():
        print(y)
    inner()
outer()
```
**🔹 Global (G)**

Module level এ declare করা variable।
```python
z = 30  # Global

def show():
    print(z)
show()
```
**🔹 Built-in (B)**

Python এর default function বা keyword।
```python
print(len("Python"))  # len হলো Built-in
```
✅ LEGB Rule

Python variable lookup করে এই order এ:
Local → Enclosing → Global → Built-in

> সংক্ষেপে: যখন Python কোনো variable খোঁজে, তখন প্রথমে function এর ভিতরে (Local), তারপর outer function (Enclosing), তারপর module (Global), আর শেষে built-in functions এ (Built-in) খুঁজে।

**৯. `__new__`, `__init__`, `__call__`**

🔹`__new__`: Object তৈরি করে → memory allocate করে।
```python
class A:
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)
    def __init__(self, x):
        print("__init__ called")
        self.x = x

a = A(5)
# Output: __new__ called → __init__ called
```
🔹`__init__`: Object initialize করে → attribute set করে।
```python
class B:
    def __init__(self, name):
        print("Hello", name)

b = B("Python")  
# Output: Hello Python
```
🔹`__call__`: Object কে function এর মতো call করলে এই method চলে।
```python
class C:
    def __call__(self, y):
        print("Called with", y)

c = C()
c(10)  
# Output: Called with 10
```

**১০. classmethods, staticmethods, instance methods**

**🔹 Instance Method**

- সবচেয়ে বেশি ব্যবহৃত।
- প্রথম parameter সবসময় self (object কে reference করে)।
```python
class MyClass:
    def instance_method(self):
        return "I am an instance method", self

obj = MyClass()
print(obj.instance_method())  
# Output: ("I am an instance method", <MyClass object>)
```
**🔹 Class Method**

- Class level এ কাজ করে।
- প্রথম parameter cls (class কে reference করে)।
- @classmethod দিয়ে define করা হয়।
```python
class MyClass:
    count = 0
    @classmethod
    def class_method(cls):
        cls.count += 1
        return f"Class count = {cls.count}"

print(MyClass.class_method())  
# Output: Class count = 1
```
**🔹 Static Method**

- Class বা instance কোনো reference নেয় না।
- সাধারণ function এর মতো, কিন্তু class এর ভিতরে থাকে।
- @staticmethod দিয়ে define করা হয়।
```python
class MyClass:
    @staticmethod
    def static_method(x, y):
        return x + y

print(MyClass.static_method(3, 4))  
# Output: 7
```
> সংক্ষেপে:
>- Instance Method → object এর সাথে কাজ করে (self)।
>- Class Method → class এর সাথে কাজ করে (cls)।
>- Static Method → independent function, শুধু class namespace এর মধ্যে থাকে।

**১১. Multiple inheritance এবং MRO (Method Resolution Order)**

*Multiple Inheritance*

একটা class একাধিক parent class থেকে inherit করতে পারে।
```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):  # Multiple inheritance
    pass

obj = C()
obj.show()   # Output: A
```
> এখানে C class এ show() method দুটোই আছে (A, B থেকে), কিন্তু Python MRO ফলো করে A → B order অনুযায়ী A.show() নেয়।

*MRO (Method Resolution Order)*

Python খুঁজে method কোথায় আছে — তার জন্য C3 linearization algorithm use করে।
Order দেখা যায় `__mro__` বা mro() দিয়ে।
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```
> সংক্ষেপে:
>- Multiple inheritance → class একাধিক parent থেকে inherit করতে পারে।
>- MRO → method খোঁজার order (Local → Left → Right → Up)।

**১২. Descriptor Protocol কী?**

Descriptor হলো এমন object যেটার মধ্যে special method থাকে:

>`__get__`(self, instance, owner) → value read করার সময়

>`__set__`(self, instance, value) → value set করার সময়

>`__delete__`(self, instance) → value delete করার সময়

 যদি কোনো class এ এই method গুলো থাকে, আর অন্য class এর attribute হিসেবে ব্যবহার হয়, তখনই সেটা descriptor।
```python
class MyDescriptor:
    def __get__(self, instance, owner):
        print("Getting value...")
        return instance._value
    
    def __set__(self, instance, value):
        print("Setting value...")
        instance._value = value
    
    def __delete__(self, instance):
        print("Deleting value...")
        del instance._value

class MyClass:
    attr = MyDescriptor()  # Descriptor ব্যবহার
    
    def __init__(self, value):
        self.attr = value   # __set__ call হবে

obj = MyClass(10)     # Setting value...
print(obj.attr)       # Getting value... → 10
del obj.attr          # Deleting value...
```
> সংক্ষেপে:
>- Descriptor Protocol → `__get__`, `__set__`, `__delete__` method define করা।
>- Property, classmethod, staticmethod internally descriptor দিয়েই implement করা হয়েছে।

**১৩. property এর ব্যবহার**

- property দিয়ে attribute access control করা যায় (getter, setter, deleter)।
- Encapsulation সহজ হয়।

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):       # getter
        return self._name

    @name.setter
    def name(self, value): # setter
        self._name = value

p = Person("Rahim")
print(p.name)   # Rahim
p.name = "Karim"
print(p.name)   # Karim
```
> সংক্ষেপে: property method কে attribute access এর মতো ব্যবহার করতে দেয়।

**১৪. Explain Namespaces**

- Namespace হলো একটা naming system, যেখানে নাম (identifier) → object এর সাথে mapping হয়ে থাকে।
- Python এ প্রতিটি নাম আলাদা namespace এ রাখা হয়, যাতে নাম conflict না হয়।

 Namespace এর ধরন ->

- Local Namespace → Function এর ভিতরের variable
- Global Namespace → Module level variable
- Built-in Namespace → Python এর built-in functions/keywords
```python
x = 10   # Global namespace

def func():
    y = 20   # Local namespace
    print(y)

func()
print(x)
print(len)  # Built-in namespace
```

**১৫. Private এবং Protected variable naming**

- Protected (_var) → conventionally বাইরে থেকে access না করা উচিত, তবে করা যায়।
- Private (__var) → name mangling হয়, direct access করা যায় না (access করতে হয় _ClassName__var দিয়ে)।

```python
class Demo:
    def __init__(self):
        self._prot = "Protected"
        self.__priv = "Private"

obj = Demo()
print(obj._prot)        # Allowed (but discouraged)
print(obj._Demo__priv)  # Name mangling দিয়ে access
```

**১৬. PYTHON Environment Variables**

- PYTHONHOME → Python interpreter এর root path নির্ধারণ করে।
- PYTHONSTARTUP → Python shell চালুর সময় যে script run হবে সেটার path।
- PYTHONBREAKPOINT → ডিফল্ট debugger সেট করতে ব্যবহৃত হয়।
- PYTHONIOENCODING → I/O operations এর জন্য কোন encoding ব্যবহার হবে তা নির্ধারণ করে।
- PYTHONWARNINGS → warning message কিভাবে handle হবে সেটা control করে।
- PYTHONHASHSEED → hash randomization এর জন্য seed সেট করে (security এর জন্য)।
- PYTHONUNBUFFERED → stdout/stderr কে unbuffered করে (output সাথে সাথে দেখায়)।

**১৭. Virtual Environment এর গুরুত্ব**

- Project specific dependencies isolate করে।
- System Python environment safe রাখে।
- Version conflicts prevent করে।

**১৮. Identity এবং Equality operator**

- is → object identity (memory address check)
- == → value equality

**১৯. Pickle এবং Copy module**

- pickle: Python objects serialize/unserialize
- copy: shallow copy (copy.copy), deep copy (copy.deepcopy)

**২০. super() inheritance এ কিভাবে কাজ করে**

- super() → parent class এর method call করতে ব্যবহৃত হয়।
- Multiple inheritance এ MRO (Method Resolution Order) অনুযায়ী parent খোঁজা হয়।

```python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        super().hello()   # parent class (A) call
        print("B")

B().hello()

# Output:
A
B
```
> এখানে B().hello() → প্রথমে A.hello() call হয়, তারপর B.hello() print করে।

**২১. Exception Handling এবং Re-throwing**

- Exception Handling → try-except block দিয়ে runtime error handle করা হয়।
- Re-throwing → exception ধরার পর আবার raise করে parent বা outer scope এ পাঠানো যায়।

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Caught exception:", e)
        raise   # Re-throw

try:
    divide(5, 0)
except ZeroDivisionError:
    print("Handled outside")

# Output
Caught exception: division by zero
Handled outside
```

> সংক্ষেপে:
>- try-except → handle করে
>- raise → আবার exception throw করে

---
## Basic Questions

**1. Python এর কি advantage?**

- Python interpreted, dynamically typed, high-level language।
- Advantages: সহজ syntax, rich library, cross-platform, OOP support।

**2. Python কি dynamically typed language?**

হ্যাঁ। variable declare করার সময় type উল্লেখ করতে হয় না।
```python
x = 10
x = "Hello"  # allowed
```
**3. Difference between list, tuple, set, dict**

- List → ordered, mutable
- Tuple → ordered, immutable
- Set → unordered, unique elements
- Dict → key-value pair, unordered
```python
l = [1,2]; t = (1,2); s={1,2}; d={'a':1}
```

**4. Python এ *args এবং **kwargs কি?**

- *args → positional arguments, tuple আকারে আসে
- **kwargs → keyword arguments, dict আকারে আসে

```python
def f(*args, **kwargs):
    print(args, kwargs)
f(1,2,a=3)
# Output: (1,2) {'a':3}
```

**5. Python এ deep copy এবং shallow copy**

- Shallow copy → nested object copy নয়
- Deep copy → সম্পূর্ণ copy, nested object সহ
```python
import copy
lst1=[[1,2]]; lst2=copy.deepcopy(lst1)
```

**6. Python এর iterable এবং iterator**

- Iterable → looping করা যায় (list, tuple)
- Iterator → `__iter__`() + `__next__`() implement করা object
```python
it = iter([1,2])
next(it)  # 1
```

**7. Difference between Python 2 and Python 3**

- Python 3 → print() function, unicode default, division float
- Python 2 → print statement, ascii default, integer division

**8. Python এ memory management কিভাবে হয়?**

Heap memory, reference counting + garbage collector, PyMalloc allocator

**9. Python এ pass by object reference / pass by value difference**

- Immutable → new object তৈরি হয় (pass by value effect)
- Mutable → original object modify হয় (pass by reference effect)
```python
def f(x): x+=1
def g(lst): lst.append(4)
```

**10. Python এ lambda function কি?**

Anonymous function, single line, inline
```python
f = lambda x: x+1
print(f(4))  # 5
```

**11. Python এ map(), filter(), reduce() difference**

- map → function apply to each element
- filter → filter condition satisfy element
- reduce → cumulative operation
```python
from functools import reduce
reduce(lambda x,y:x+y, [1,2,3])  # 6
```

**12. Python এ decorator কি?**

Function কে modify বা extend করতে পারে
```python
def deco(f): return lambda: f()
@deco
def hello(): print("Hi")
hello()   # Hi
```
**13. Python এ generator কি?**

yield ব্যবহার করে lazy evaluation, memory efficient
```python
def gen(): yield 1; yield 2
for x in gen(): print(x)

#Output
1
2
```
**14. Python এ with statement / context manager**

Resource management, file handling, automatic close
```
with open('test.txt') as f:
    data = f.read()
```

**15. Python এ mutable এবং immutable data type**

- Mutable → list, dict, set
- Immutable → int, float, string, tuple

**16. Python এ PEP8 কি?**

- Python এর coding standard guide
- Variable, function, indentation, naming convention define করে

**17. Python এ virtual environment importance**

- Project-wise dependency isolation
- Python package conflict এড়ায়

**18. Python এ pip কি?**

Python package manager, library install/update/remove করতে ব্যবহৃত হয়

**19. Python এ exception hierarchy**

- Base → BaseException → Exception → ValueError, TypeError ইত্যাদি
- try-except block দিয়ে handle করা হয়

**20. Python এ Pythonic way কি?**

Clean, readable, efficient code writing style
```python
# Pythonic
squares = [x*x for x in range(5)]
```