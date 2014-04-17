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

# pass
print "press ctrl + c to continue"

while True:
    pass
