#!/usr/bin/env python3
import matplotlib.pyplot as plt
import timeit

# Dirty hack for passing grow list size
g_base = 0


def test1():
    l = []
    for i in range(g_base):
        l = l + [i]
    return l


def test2():
    l = []
    for i in range(g_base):
        l.append(i)
    return l


def test3():
    l = [i for i in range(g_base)]
    return l


def test4():
    l = list(range(g_base))
    return l

if __name__ == "__main__":
    t_record = [[0 for x in range(10)] for x in range(4)]
    t_degree = [i for i in range(10)]
    t_lines = ('concat', 'append', 'comprehension', 'list range')

    # Collect data (execute time)
    for i in range(1, 11):
        g_base = 120 * i
        t_degree[i - 1] = g_base

        print("\n\nAdd list with %d" % g_base)
        t1 = timeit.Timer("test1()", "from __main__ import test1")
        t_elapse = t1.timeit(number=1000)
        t_record[0][i - 1] = t_elapse
        print("concat ", t_elapse, "milliseconds")

        t2 = timeit.Timer("test2()", "from __main__ import test2")
        t_elapse = t2.timeit(number=1000)
        t_record[1][i - 1] = t_elapse
        print("append ", t_elapse, "milliseconds")

        t3 = timeit.Timer("test3()", "from __main__ import test3")
        t_elapse = t3.timeit(number=1000)
        t_record[2][i - 1] = t_elapse
        print("comprehension ", t_elapse, "milliseconds")

        t4 = timeit.Timer("test4()", "from __main__ import test4")
        t_elapse = t4.timeit(number=1000)
        t_record[3][i - 1] = t_elapse
        print("list range ", t_elapse, "milliseconds")

    # Prepare to plot
    plt.xlabel('Create size')
    plt.ylabel('Create time')
    for i in range(4):
        plt.text(t_degree[9], t_record[i][9], t_lines[i])
        plt.plot(t_degree, t_record[i], label=t_lines[i])

    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()
