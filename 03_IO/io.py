#/usr/bin/env python
# Test pretty format: "{n-th arg: spaces}".format(var...)
for i in range(1, 21):
    for j in range(1, 21):
        print("{0:2d} x {1:2d} = {2:4d}".format(i, j, (i * i)))
