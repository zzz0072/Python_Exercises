#!/usr/bin/env python
import sys

print("argv: %d" % len(sys.argv))

# Object related test
# type and id are unique
# ref: https://docs.python.org/2/reference/datamodel.html
# mutable object: value can be changed
# immutable object: value can NOT be changed after created
#                   This means readonly
#   ex: string, numbers, tuple

print(type(sys.argv))
print(id(sys.argv))
print(type(sys.argv) is list)

my_list = range(10)
print(my_list)
del my_list[-1]
print(my_list)

if len(sys.argv) != 2:
    print("%s filename" % sys.argv[0])
    raise SystemExit(1)

file = open(sys.argv[1], "w")

line = []
while True:
    line = sys.stdin.readline()
    if line == "quit\n":
        break
    file.write(line)
file.close()

print("\nok. start to dump %s:"  % sys.argv[1])
for line in open(sys.argv[1]):
    print line.rstrip()

file = open(sys.argv[1])
lines = file.readlines()
file.close()

print(lines)

fval = [float(line) for line in lines]

print(fval)
print("len: %d" % len(fval))

for i in range(len(fval)):
    print i, " ", fval[i]
