#!/usr/bin/env python
# every thing is unique
print(set("aaabbb"))

# set operartion
set_a = set(range(-1, 4))
set_b = set(range(1, 5))

print(set_a - set_b)
print(set_a | set_b)
print(set_a & set_b)
print(set_a ^ set_b)

