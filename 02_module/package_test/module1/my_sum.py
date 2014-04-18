#/usr/bin/env python
from ..module2 import my_print

def my_sum(x, y):
    result = x + y
    my_print.my_print(result)

# To run method alone
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("%s str1 str2" % sys.argv[0])
        raise SystemExit(1)

    my_sum(sys.argv[1], sys.argv[2])


