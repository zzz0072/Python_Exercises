#/usr/bin/env python
# method 1
import module
print (module.my_sum("I am", " zzz 1"))

# method 2, no seed to include namespace
from module import my_sum
print (my_sum("I am", " zzz 2"))

# method 3, no seed to include namespace
from module import *
print (my_sum2("I am", " zzz 3"))
