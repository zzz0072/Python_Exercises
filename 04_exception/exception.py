#/usr/bdin/env python
import random

# File name source
f_num = [chr(48 + x) for x in range(1, 10)]

# A to Z
f_alphabat = [chr(65 + x) for x in range(0, 26)]

# Make up filename in 5 chars
file_name = []
for i in range(1, 6):
    use_num = random.randint(0, 1)
    if use_num:
        file_name.append(random.choice(f_num))
    else:
        file_name.append(random.choice(f_alphabat))

# Convert to string
file_name = "".join(file_name)

print(file_name)

# Show a open file exception with details
try:
    file = open(file_name)
except IOError as file_err:
    print(file_err)

# Fire a self exception
class my_error(Exception):
    def __init__(self, errno):
        self.value = errno
    def __str__(self):
        return repr(self.value)

try:
    raise my_error("ouch...");
except my_error as e:
    print(e)
