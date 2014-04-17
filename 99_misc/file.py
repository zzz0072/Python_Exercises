#/usr/bin/env python
import sys
print ("Enter file name:".rstrip())
name = sys.stdin.readline()

name = name.rstrip()
file = open(name, "w")

line = sys.stdin.readline()
while line != "quit\n":
    line = sys.stdin.readline()
    file.write(line)

file.close();

print("ok. start to dump %s"  % name)
for line in open(name):
    print line.rstrip()

