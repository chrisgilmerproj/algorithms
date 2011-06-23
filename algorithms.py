#!/usr/local/bin/python

import random
import time


def print_timing(func):
    """ A decorator to determine how long an algorithm takes to complete """
    def wrapper(*arg, **kwargs):
        t1 = time.clock()
        res = func(*arg, **kwargs)
        t2 = time.clock()
        print '%s\ttook %0.3fms' % (func.func_name, (t2 - t1) * 1000.0)
        return res
    return wrapper


def gen_array(x):
    return [random.randint(1, x) for i in xrange(0, x)]


@print_timing
def insertion_sort(A):
    """
    Best:    n
    Average: n^2
    Worst:   n^2
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(A):
    """
    Best:    nlogn
    Average: nlogn
    Worst:   nlogn
    """
    if len(A) < 2:
        return A
    middle = len(A) / 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right)


@print_timing
def merge_time(A):
    """ Method for timing merge_sort """
    return merge_sort(A)


@print_timing
def bubble_sort(A):
    """
    Best:    n
    Average: n^2
    Worst:   n^2
    """
    for i in range(0, len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


@print_timing
def quicksort_time(A):
    return quicksort(A)


def quicksort(A):
    """
    Best:    nlogn
    Average: nlogn
    Worst:   n^2
    """
    if A == []:
        return A
    q = A.pop(random.randrange(len(A)))
    left = quicksort([l for l in A if l < q])
    right = quicksort([l for l in A if l < q])
    return left + [q] + right


@print_timing
def selection_sort(A):
    for x in range(0, len(A) - 1):
        q = x
        for y in range(x + 1, len(A)):
            if A[y] < A[q]:
                q = y
        A[x], A[q] = A[q], A[x]


@print_timing
def python_sort(A):
    A.sort()


def test(x):
    A = gen_array(x)
    insertion_sort(A)

    A = gen_array(x)
    merge_time(A)
    bubble_sort(A)

    A = gen_array(x)
    quicksort_time(A)
    selection_sort(A)
    python_sort(A)

try:
    from IPython.Shell import IPShellEmbed
    IPShellEmbed()(local_ns=locals())
except:
    import code
    code.interact()
