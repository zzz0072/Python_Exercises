#!/usr/bin/env python
import sys

print ("argv: %d" % len(sys.argv))

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

for i in fval:
    print i
