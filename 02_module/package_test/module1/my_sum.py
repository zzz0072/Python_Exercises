#/usr/bin/env python
def my_sum(x, y):
    return x + y

def my_sum2(x, y):
    return x + y

# To run method alone
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("%s str1 str2" % sys.argv[0])
        raise SystemExit(1)

    print(my_sum(sys.argv[1], sys.argv[2]))


