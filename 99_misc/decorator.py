#/usr/bin/env python
def my_func1(callback):
    def func_wrapper(x):
        print("my_func1: {0} ".format(callback(x)))
    return func_wrapper

@my_func1
def my_func2(x):
    return x

# Actuall call sequence is similar to:
# deco = my_func1(my_func2)
# deco("test") => func_wrapper("test")
my_func2("test")

#-------------------------------------------
# Test decorator with parameter

def dec_param(param):
    def my_func3(callback):
        def func_wrapper(x):
            print("my_func3: {0} {1} ".format(param, callback(x)))
        return func_wrapper
    return my_func3

@dec_param("tag")
def my_func4(x):
    return x

# Actuall call sequence is similar to:
# deco = dec_pram("tag", my_func3(my_func4))
# deco("test") => func_wrapper("test")
my_func4("test")
