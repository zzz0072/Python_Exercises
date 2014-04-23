#/usr/bin/env pyhon
def my_add(x, y):
    # doctest usage
    # >>> statement
    # expected output
    ''' Doc test
    >>> my_add(1, 2)
    3
    >>> my_add("A ", "Book")
    'A Book'
    '''

    return x + y

def my_func():
    '''
    >>> my_func()
    my_func
    '''
    print "my_func"

if __name__ == '__main__':
    # assert without __debug__
    try:
        assert my_add(1, 2) == 4, "Add failure"
    except AssertionError as err:
        print(err)
        print("----------------------------")

    # doctest
    import doctest
    doctest.testmod()
