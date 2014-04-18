#/usr/bin/env python
def my_print(x):
    print x

# To run method alone
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("%s str1" % sys.argv[0])
        raise SystemExit(1)

    print(my_print(sys.argv[1]))
