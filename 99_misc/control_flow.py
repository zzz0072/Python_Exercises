#!/usr/bin/env python
# function
def sum(op1, op2):
    return op1 + op2

my_sum = sum
print my_sum(1, 2)
print my_sum("I am ", "zzz");

# Default value in a fuction
init = 12
def accumulate(val = init):
    val += val
    return val

my_accu = accumulate
init = 11
print my_accu() # is 12 + 12 rather than 11 + 11

# Default value in a function 2
def my_func(op1, op2 = '2', op3 = '3'): # non-default argument first
    return op1 + op2 + op3

print my_func('3')
print my_func('1', op2 = 'zzz')
print my_func('1', op3 = 'xxx')

# variable argument
def var_arg(*args):
    print args

var_arg(1, 2, 3, 4 ,5)
var_arg("I am ", "zzz")
var_arg(range(3,7))

# Funtional ? programing: filter
def f_callback(x):
    return x > 0  # a condition

print filter(f_callback, range(-5, 10))


# Funtional ? programing: map
def m_callback(x):
    return x * x # an action

print map(m_callback, range(-5, 10))

# Funtional ? programing: reduce
def r_callback(x, y):
    return x + y # binary operator

print reduce(r_callback, range(1, 10)) # This sum up 1 to 10

# pass
print "press ctrl + c to continue"

while True:
    pass
