#!/usr/bin/env python3
def reverse_str(string):
    if len(string) == 1:
        return string
    else:
        return reverse_str(string[1:]) + string[0]


if __name__ == "__main__":
    print(reverse_str("asdf"))
    print(reverse_str("smart"))
