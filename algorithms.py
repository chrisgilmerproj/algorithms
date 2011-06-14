#!/usr/local/bin/python

import random, time

def print_timing(func):
	""" A decorator to determine how long an algorithm takes to complete """
	def wrapper(*arg,**kwargs):
		t1 = time.clock()
		res = func(*arg,**kwargs)
		t2 = time.clock()
		print '%s\ttook %0.3fms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper

def gen_array(x):
	l = []
	for i in xrange(0,x): l.append(random.randint(1,x))
	return l

@print_timing
def insertion_sort(A):
	"""
	Best:	 n
	Average: n^2
	Worst:   n^2
	"""
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

def merge(left,right):
	result = []
	i,j = 0,0
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
	Best:	 nlogn
	Average: nlogn
	Worst:	 nlogn
	"""
	if len(A) < 2:
		return A
	middle = len(A)/2
	left   = merge_sort(A[:middle])
	right  = merge_sort(A[middle:])
	return merge(left,right)

@print_timing
def merge_time(A):
	""" Method for timing merge_sort """
	return merge_sort(A)

@print_timing
def bubble_sort(A):
	"""
	Best:	 n
	Average: n^2
	Worst:	 n^2
	"""
	for i in range(0,len(A)-1):
		for j in range(len(A)-1,i,-1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
	return A


def test(x):
	A = gen_array(x)
	insertion_sort(A)
	merge_time(A)
	bubble_sort(A)

try:
	from IPython.Shell import IPShellEmbed
	IPShellEmbed()(local_ns=locals())
except:
	import code
	code.interact()

