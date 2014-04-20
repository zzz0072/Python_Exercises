#/usr/bin/env python
# Test yield generator
def my_double(arr):
    for i in arr:
        yield i * 2

for i in my_double(range(1, 10)):
    print("{0} ".format(i)),

print("\n"),

# Text iteration
i = iter(my_double(range(10, 21)))
print i
for j in range (1, 10):
    print("{0} ".format(i.next())),

