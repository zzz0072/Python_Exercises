#/usr/bin/env python
# Test pretty format: "{n-th arg: spaces}".format(var...)
for i in range(1, 21):
    for j in range(1, 21):
        print("{0:2d} x {1:2d} = {2:4d}".format(i, j, (i * i)))

# To string without new line test and rjust alignment for pretty format
print("To string without new line test and rjust alignment for pretty format")
for i in range(1, 21):
    for j in range(1, 21):
        print(repr(i).rjust(2)),  # , means no new line
        print(repr(j).rjust(2)),
        print(repr(i*j).rjust(4)) # This do not have ,
