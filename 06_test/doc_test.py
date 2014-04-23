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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
