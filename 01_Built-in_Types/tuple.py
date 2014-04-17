#!/usr/bin/env python
import sys
import pickle

# Check argument
if len(sys.argv) != 2:
    print("%s filename" % sys.argv[0])
    raise SystemExit(1)

# Write tuples
file = open(sys.argv[1], "wb");
line = []
while True:
    print("Enter name, age, score (ex: zzz, 16, 90) or quit");
    line = sys.stdin.readline()
    if line == "quit\n":
        break

    raws = line.split(",")
    name = raws[0]
    age = int(raws[1])
    score = int(raws[2])

    record = (name, age, score)
    pickle.dump(record, file)

file.close()

# Read back
file = open(sys.argv[1], "rb");
while True:

    try:
        record = pickle.load(file)
        print record
        name, age, score= record
        print("name = %s" % name)
        print("name = %d" % age)
        print("name = %d" % score)
    except (EOFError):
        break

file.close()
