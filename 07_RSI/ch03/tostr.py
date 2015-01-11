#!/usr/bin/env python3
def toStr(num, base):
    digitStr = "0123456789ABCDEF"
    if num < base:
        return digitStr[num]
    else:
        return toStr(num // base, base) + digitStr[num % base]


if __name__ == "__main__":
    print(toStr(1200, 10))
    print(toStr(255, 16))
