#/usr/bin/env python
# for and if
print ([x for x in range(-10, 10) if x > 0])

# for and if with tuple
print ([(x, y) for x in range(-10, 10) if x > 0 \
               for y in range(1, 8)])

# call functions
def double(x):
    return x * 2
print [double(x) for x in range(1, 5)]

# single action
print [x * 2 for x in range(1, 5)]

# nested lists, colum then row
print [[x for x in range(-3, 3)] for x in range(1, 5)]

# nested list 2
mat = [[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]]

print [[row[i] for row in mat] for i in range(len(mat) + 1)]

