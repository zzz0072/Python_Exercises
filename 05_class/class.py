#/usr/bin/env python
#------------------------------------------------------------------------------
# Test Doc
class foo:
    "This is a example:"

i = foo()
print(i.__doc__)

#------------------------------------------------------------------------------
# Test data member
class bar:
    x = 10
    y = 20
    __hidden = 30 # Actually symbol is _bar__hidden, so can not write ousite?
    def get_hidden(self):
        return self.__hidden

    def set_hidden(self, x):
        self.__hidden = x

i = bar()
i.x = 10
i.y = 20
print("{0} {1} {2}".format(i.x, i.y, i.get_hidden()))
i.set_hidden("zzz")
print("{0} {1} {2}".format(i.x, i.y, i.get_hidden()))

# Modify hidden data diretly, not work
i.__hidden = 11
print("new hidden: {0} {1} {2}".format(i.x, i.y, i.get_hidden()))

# with _bar_hidden
i._bar__hidden = "xxx"
print("new hidden with _bar prefix: {0} {1} {2}".format(i.x, i.y, i.get_hidden()))

# Second instance, the value is new now
j = bar()
print("{0} {1} {2}".format(j.x, j.y, j.get_hidden()))


#------------------------------------------------------------------------------
# Function and inherit
class base:
    def my_func(self): # MUST at lease self!
        print("my_func: {0}".format(self))
    def my_func2(self):
        print(self)

class derived(base):
    def my_func2(self):
        print("Overwrite: {0}".format(self))
    def my_func3(self):
        print(self)

print("base")
tmp = base()
tmp.my_func()

print("derived")
dved = derived()
dved.my_func()
dved.my_func2()
dved.my_func3()

#------------------------------------------------------------------------------
# Test constructor
class con_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_vars(self):
        return self.x, self.y

    def set_vars(self, x, y):
        self.x = x
        self.y = y

i = con_class(1, 2)
print(i.get_vars())

i.set_vars(3, 4)
print(i.get_vars())

#------------------------------------------------------------------------------
# Test as a record
class rec:
    pass

my_rec = rec()
my_rec.name = "zzz"
my_rec.age  = 12345

print("rec: {0} {1}".format(my_rec.name, my_rec.age))

#------------------------------------------------------------------------------
# Test exception
class first:
    pass

class second(first):
    pass

class third(second):
    pass

for ins in [first, second, third]:
    # MUST with reversed order
    # ref: https://docs.python.org/2/tutorial/classes.html#exceptions-are-classes-too
    try:
        raise ins()
    except third:
        print(ins)
    except second:
        print(ins)
    except first:
        print(ins)

